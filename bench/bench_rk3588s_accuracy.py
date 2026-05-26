"""
GLiNER full NER pipeline benchmark on RK3588S.
Tests fp16 vs int8 accuracy using Wikipedia Taiwan multilingual test data.
"""
import os, sys, time
import numpy as np
import onnxruntime as ort
from tokenizers import Tokenizer

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from test_data_taiwan import TEST_CASES

BASE = "/mnt/nvme/openab/data/~/gliner-model"
TOKENIZER = f"{BASE}/fp16/tokenizer.json"


def load_variant(variant: str):
    suffix_map = {"fp16": "_fp16", "int8": "_int8", "fp32": "_fp32_full"}
    suffix = suffix_map.get(variant, f"_{variant}")
    
    opts = ort.SessionOptions()
    opts.graph_optimization_level = ort.GraphOptimizationLevel.ORT_ENABLE_ALL
    
    models = {}
    for name in ["encoder", "span_rep", "classifier"]:
        path = os.path.join(BASE, variant, f"{name}{suffix}.onnx")
        if not os.path.exists(path):
            print(f"⚠️  {name} not found: {path}")
            return None
        models[name] = ort.InferenceSession(path, opts, providers=["CPUExecutionProvider"])
        inputs = [(i.name, i.shape, i.type) for i in models[name].get_inputs()]
        outputs = [(o.name, o.shape, o.type) for o in models[name].get_outputs()]
        print(f"  {name}: inputs={inputs}")
        print(f"         outputs={outputs}")
    
    return models


def run_gliner(models, tokenizer, text, labels, max_len=512):
    """Full GLiNER NER pipeline: encoder → span_rep → classifier."""
    # Build input
    schema = " ".join(f"[E] {l}" for l in labels)
    full_input = f"[P] entities ( {schema} ) [SEP_TEXT] {text}"
    
    encoded = tokenizer.encode(full_input)
    # Truncate to max_len (span_rep requires exact 512)
    ids = encoded.ids[:max_len]
    ids = ids + [0] * (max_len - len(ids))
    input_ids = np.array([ids], dtype=np.int64)
    n_tokens = min(sum(encoded.attention_mask), max_len)
    
    # 1. Encoder: input_ids → last_hidden_state (1, 512, 768)
    t0 = time.time()
    hidden = models["encoder"].run(None, {"input_ids": input_ids})[0]
    encoder_ms = (time.time() - t0) * 1000
    
    # 2. Build span indices: all (start, end) pairs, max span width 8
    max_span_width = 8
    span_indices = []
    for i in range(min(n_tokens, max_len)):
        for j in range(i, min(i + max_span_width, n_tokens, max_len)):
            span_indices.append([i, j])
    
    span_idx = np.array([span_indices], dtype=np.int64)  # (1, num_spans, 2)
    num_spans = len(span_indices)
    
    # 3. Span representation: hidden + span_idx → span_embeddings
    t0 = time.time()
    span_embeddings = models["span_rep"].run(
        None,
        {
            "last_hidden_state": hidden,
            "span_idx": span_idx,
        }
    )[0]
    span_ms = (time.time() - t0) * 1000
    
    # 4. Classifier: span_embeddings → logits
    t0 = time.time()
    logits = models["classifier"].run(
        None,
        {"span_embeddings": span_embeddings}
    )[0]
    class_ms = (time.time() - t0) * 1000
    
    # 5. Extract entities
    # logits shape: (1, seq_len, 8, 1) — need to figure out mapping
    entities = []
    
    # The classifier outputs per-span scores
    # Need to reshape based on actual output
    if len(logits.shape) == 4:
        # (1, seq_len, max_span_width, 1) → per-position scores
        # Use argmax approach
        pass
    elif len(logits.shape) == 2:
        # (num_spans, 1) → one score per span
        for idx in range(min(num_spans, logits.shape[0])):
            score = float(logits[idx, 0])
            if score > 0.3:
                start, end = span_indices[idx]
                tokens = encoded.tokens[start:end+1]
                entity_text = "".join(t.replace("▁", " ").replace("##", "") for t in tokens).strip()
                if entity_text:
                    # Determine label by position in schema
                    entities.append({
                        "text": entity_text,
                        "label": labels[min(idx % len(labels), len(labels)-1)] if labels else "unknown",
                        "score": score,
                        "span": (start, end),
                    })
    
    return {
        "entities": entities,
        "encoder_ms": encoder_ms,
        "span_ms": span_ms,
        "class_ms": class_ms,
        "total_ms": encoder_ms + span_ms + class_ms,
        "num_spans": num_spans,
        "n_tokens": n_tokens,
        "logits_shape": logits.shape,
    }


def score_recall(predicted, expected):
    """Fuzzy recall matching."""
    if not expected:
        return 1.0, 0, 0, []
    
    found = []
    for exp in expected:
        exp_text = exp["text"].lower()
        exp_label = exp["label"]
        matched = False
        for pred in predicted:
            pred_text = pred["text"].lower()
            pred_label = pred["label"]
            if (exp_text in pred_text or pred_text in exp_text) and exp_label == pred_label:
                matched = True
                break
        found.append(matched)
    
    recall = sum(found) / len(expected)
    return recall, sum(found), len(expected), found


def main():
    tokenizer = Tokenizer.from_file(TOKENIZER)
    results = {}
    
    for variant in ["fp16", "int8"]:
        print(f"\n{'='*60}")
        print(f"Loading {variant.upper()} models...")
        models = load_variant(variant)
        if models is None:
            continue
        
        variant_results = []
        total_time = 0
        
        for i, case in enumerate(TEST_CASES):
            lang = case["lang"]
            text = case["text"]
            labels = case["labels"]
            expected = case["expected"]
            
            result = run_gliner(models, tokenizer, text, labels)
            recall, found, total_exp, matched = score_recall(result["entities"], expected)
            total_time += result["total_ms"]
            
            cr = {
                "lang": lang, "recall": recall, "found": found,
                "expected": total_exp, "total_ms": result["total_ms"],
                "encoder_ms": result["encoder_ms"],
                "num_spans": result["num_spans"],
                "entities": result["entities"],
                "logits_shape": result["logits_shape"],
            }
            variant_results.append(cr)
            
            status = "✅" if recall >= 0.5 else "⚠️" if recall >= 0.3 else "❌"
            ent_str = ", ".join(f"{e['text']}/{e['label']}" for e in result["entities"][:5])
            print(f"  {status} [{i:2d}] {lang:5s} recall={recall:.0%} ({found}/{total_exp}) "
                  f"{result['total_ms']:.0f}ms (enc={result['encoder_ms']:.0f}) | {ent_str}")
        
        results[variant] = variant_results
        avg_recall = np.mean([r["recall"] for r in variant_results]) * 100
        print(f"\n  📊 {variant.upper()}: avg recall {avg_recall:.1f}%, total {total_time:.0f}ms")
    
    if len(results) == 2:
        print(f"\n{'='*60}")
        print("📊 FP16 vs INT8 Accuracy (RK3588S, Wikipedia Taiwan)")
        print(f"{'='*60}")
        print(f"{'#':>2} {'Lang':<6} {'FP16':>8} {'INT8':>8} {'Δ':>7}")
        print("-" * 35)
        for i in range(len(TEST_CASES)):
            fp16_r = results["fp16"][i]["recall"] * 100
            int8_r = results["int8"][i]["recall"] * 100
            delta = int8_r - fp16_r
            arrow = "✅" if delta >= -5 else "⚠️" if delta >= -20 else "❌"
            print(f"{i:2d} {TEST_CASES[i]['lang']:<6} {fp16_r:>6.0f}% {int8_r:>6.0f}% {delta:>+5.0f}% {arrow}")
        
        fp16_avg = np.mean([r["recall"] for r in results["fp16"]]) * 100
        int8_avg = np.mean([r["recall"] for r in results["int8"]]) * 100
        print("-" * 35)
        print(f"   AVG   {fp16_avg:>6.1f}% {int8_avg:>6.1f}% {int8_avg-fp16_avg:>+5.1f}%")


if __name__ == "__main__":
    main()
