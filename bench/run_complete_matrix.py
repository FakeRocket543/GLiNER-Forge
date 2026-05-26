"""Complete comparison matrix: all model × backend × precision combinations."""
import sys, os, time, gc
from pathlib import Path
from collections import defaultdict

sys.path.insert(0, str(Path(__file__).resolve().parent))
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from test_data_taiwan import TEST_CASES

import torch

MODELS = [
    ("gliner-community/gliner_small-v2.5", "small-v2.5"),
    ("gliner-community/gliner_medium-v2.5", "medium-v2.5"),
]
WARMUP, RUNS = 2, 3
THRESHOLD = 0.3


def fuzzy_match(pred_ents, expected):
    """Recall with fuzzy matching: substring in either direction + same label."""
    hits = 0
    for exp in expected:
        for p in pred_ents:
            p_label = p.get("label", p.get("type", ""))
            p_text = p.get("text", p.get("span", ""))
            if p_label == exp["label"] and (exp["text"] in p_text or p_text in exp["text"]):
                hits += 1
                break
    return hits, len(expected)


def run_benchmark(predict_fn, label=""):
    """Run warmup + timed iterations. Returns (recall%, per_lang_recall, avg_ms, total_s)."""
    # Warmup
    for _ in range(WARMUP):
        for tc in TEST_CASES:
            try:
                predict_fn(tc["text"], tc["labels"])
            except Exception:
                pass

    # Timed runs
    total_time = 0
    for _ in range(RUNS):
        t0 = time.perf_counter()
        for tc in TEST_CASES:
            predict_fn(tc["text"], tc["labels"])
        total_time += time.perf_counter() - t0

    # Compute recall (separate pass)
    total_hits = 0
    total_expected = 0
    lang_hits = defaultdict(int)
    lang_total = defaultdict(int)
    for tc in TEST_CASES:
        preds = predict_fn(tc["text"], tc["labels"])
        h, t = fuzzy_match(preds, tc["expected"])
        total_hits += h
        total_expected += t
        lang_hits[tc["lang"]] += h
        lang_total[tc["lang"]] += t

    recall = total_hits / total_expected if total_expected else 0
    per_lang = {lang: lang_hits[lang] / lang_total[lang] if lang_total[lang] else 0
                for lang in lang_total}
    avg_ms = (total_time / RUNS / len(TEST_CASES)) * 1000
    total_s = total_time / RUNS
    return recall, per_lang, avg_ms, total_s


def test_transformer_fp32(model_name):
    from gliner import GLiNER
    model = GLiNER.from_pretrained(model_name)
    model.eval()
    predict_fn = lambda text, labels: model.predict_entities(text, labels, threshold=THRESHOLD)
    result = run_benchmark(predict_fn)
    del model; gc.collect()
    return result


def test_transformer_fp16(model_name):
    from gliner import GLiNER
    model = GLiNER.from_pretrained(model_name)
    model.eval()
    try:
        model.model.half()
    except Exception as e1:
        try:
            model.model.to(torch.float16)
        except Exception as e2:
            del model; gc.collect()
            raise RuntimeError(f"CPU FP16 unsupported: half()={e1}, to(fp16)={e2}")
    predict_fn = lambda text, labels: model.predict_entities(text, labels, threshold=THRESHOLD)
    result = run_benchmark(predict_fn)
    del model; gc.collect()
    return result


def test_transformer_bf16(model_name):
    from gliner import GLiNER
    model = GLiNER.from_pretrained(model_name)
    model.eval()
    model.model.to(torch.bfloat16)
    predict_fn = lambda text, labels: model.predict_entities(text, labels, threshold=THRESHOLD)
    result = run_benchmark(predict_fn)
    del model; gc.collect()
    return result


def test_onnx_fp32(model_name, short_name):
    from gliner import GLiNER
    save_dir = Path(f"models/onnx/{short_name}")
    onnx_path = save_dir / "model.onnx"

    if not onnx_path.exists():
        print(f"    Exporting ONNX to {save_dir}...", flush=True)
        model_pt = GLiNER.from_pretrained(model_name)
        model_pt.export_to_onnx(save_dir=str(save_dir), quantize=False)
        del model_pt; gc.collect()

    model = GLiNER.from_pretrained(str(save_dir), load_onnx_model=True)
    predict_fn = lambda text, labels: model.predict_entities(text, labels, threshold=THRESHOLD)
    result = run_benchmark(predict_fn)
    del model; gc.collect()
    return result


def test_onnx_fp16(model_name, short_name):
    save_dir = Path(f"models/onnx/{short_name}")
    onnx_path = save_dir / "model.onnx"
    fp16_path = save_dir / "model_fp16.onnx"

    if not onnx_path.exists():
        raise RuntimeError(f"ONNX model not found at {onnx_path}. Run ONNX FP32 first.")

    if not fp16_path.exists():
        print(f"    Converting to FP16...", flush=True)
        import onnx
        try:
            from onnxruntime.transformers import float16
            model_fp16 = float16.convert_float_to_float16(onnx.load(str(onnx_path)))
        except ImportError:
            try:
                from onnxconverter_common import float16
                model_fp16 = float16.convert_float_to_float16(onnx.load(str(onnx_path)))
            except ImportError:
                raise RuntimeError("Neither onnxruntime.transformers.float16 nor onnxconverter_common available")
        onnx.save(model_fp16, str(fp16_path))

    from gliner import GLiNER
    model = GLiNER.from_pretrained(str(save_dir), load_onnx_model=True, onnx_model_file="model_fp16.onnx")
    predict_fn = lambda text, labels: model.predict_entities(text, labels, threshold=THRESHOLD)
    result = run_benchmark(predict_fn)
    del model; gc.collect()
    return result


def test_mlx(model_name, short_name):
    from openmed.mlx.inference import GLiNERRelexMLXPipeline
    from huggingface_hub import snapshot_download

    # Map to MLX model
    mlx_model = "OpenMed/gliner-relex-base-v1.0-mlx"
    model_path = snapshot_download(mlx_model)
    pipeline = GLiNERRelexMLXPipeline(model_path)

    def predict_fn(text, labels):
        result = pipeline.inference(text, labels=labels, relations=[], threshold=THRESHOLD)
        return result.get("entities", [])

    result = run_benchmark(predict_fn)
    del pipeline; gc.collect()
    return result


def main():
    print(f"{'='*75}")
    print(f"  COMPLETE MATRIX BENCHMARK")
    print(f"  Models: {len(MODELS)} | Test cases: {len(TEST_CASES)} | Warmup: {WARMUP} | Timed runs: {RUNS}")
    print(f"{'='*75}\n")

    results = []  # (model_short, backend, precision, recall, per_lang, avg_ms, total_s, error)

    configs = [
        ("Transformer", "FP32", test_transformer_fp32),
        ("Transformer", "FP16", test_transformer_fp16),
        ("Transformer", "BF16", test_transformer_bf16),
        ("ONNX", "FP32", None),  # special handling
        ("ONNX", "FP16", None),  # special handling
        ("MLX", "FP32", None),   # special handling
    ]

    for model_name, short_name in MODELS:
        print(f"\n{'─'*60}")
        print(f"  Model: {short_name} ({model_name})")
        print(f"{'─'*60}")

        for backend, precision, fn in configs:
            combo = f"{short_name}/{backend}/{precision}"
            print(f"\n  [{backend} {precision}] ", end="", flush=True)
            try:
                if backend == "Transformer":
                    recall, per_lang, avg_ms, total_s = fn(model_name)
                elif backend == "ONNX" and precision == "FP32":
                    recall, per_lang, avg_ms, total_s = test_onnx_fp32(model_name, short_name)
                elif backend == "ONNX" and precision == "FP16":
                    recall, per_lang, avg_ms, total_s = test_onnx_fp16(model_name, short_name)
                elif backend == "MLX":
                    recall, per_lang, avg_ms, total_s = test_mlx(model_name, short_name)
                else:
                    continue

                results.append((short_name, backend, precision, recall, per_lang, avg_ms, total_s, None))
                print(f"Recall={recall:.1%}  Avg={avg_ms:.1f}ms/call  Total={total_s:.2f}s")
            except Exception as e:
                results.append((short_name, backend, precision, None, None, None, None, str(e)))
                print(f"FAILED: {e}")

    # ══════════════════════════════════════════════════════════════
    # TABLE 1: Overall Summary
    # ══════════════════════════════════════════════════════════════
    print(f"\n\n{'═'*75}")
    print(f"  TABLE 1: OVERALL SUMMARY")
    print(f"{'═'*75}")
    header = f"{'Model':<15} {'Backend':<13} {'Precision':<10} {'Recall%':<9} {'ms/call':<9} {'Speedup':<8} {'Status'}"
    print(header)
    print("─" * 75)

    # Reference time per model = Transformer FP32
    ref_times = {}
    for short, backend, prec, recall, _, avg_ms, _, err in results:
        if backend == "Transformer" and prec == "FP32" and err is None:
            ref_times[short] = avg_ms

    for short, backend, prec, recall, _, avg_ms, _, err in results:
        if err:
            print(f"{short:<15} {backend:<13} {prec:<10} {'—':<9} {'—':<9} {'—':<8} ✗ {err[:40]}")
        else:
            ref = ref_times.get(short, avg_ms)
            speedup = ref / avg_ms if avg_ms > 0 else 0
            print(f"{short:<15} {backend:<13} {prec:<10} {recall*100:<9.1f} {avg_ms:<9.1f} {speedup:<8.2f}x ✓")

    print("─" * 75)
    print(f"  Speedup = Transformer FP32 time / variant time (higher = faster)")

    # ══════════════════════════════════════════════════════════════
    # TABLE 2: Per-Language Breakdown
    # ══════════════════════════════════════════════════════════════
    valid = [(s, b, p, r, pl, ms, ts, e) for s, b, p, r, pl, ms, ts, e in results if e is None]
    if valid:
        # Sort by recall
        sorted_by_recall = sorted(valid, key=lambda x: x[3], reverse=True)
        top2 = sorted_by_recall[:2]
        bottom1 = sorted_by_recall[-1:]

        show_configs = top2 + bottom1

        # Get all languages
        langs = sorted(set(tc["lang"] for tc in TEST_CASES))

        print(f"\n\n{'═'*75}")
        print(f"  TABLE 2: PER-LANGUAGE RECALL (Top 2 + Bottom 1)")
        print(f"{'═'*75}")

        # Header
        lang_header = f"{'Config':<35} " + " ".join(f"{l:<7}" for l in langs)
        print(lang_header)
        print("─" * 75)

        for short, backend, prec, recall, per_lang, avg_ms, _, _ in show_configs:
            config_label = f"{short}/{backend}/{prec}"
            lang_vals = " ".join(f"{per_lang.get(l, 0)*100:<7.0f}" for l in langs)
            print(f"{config_label:<35} {lang_vals}")

        print("─" * 75)
        print(f"  Languages: {', '.join(langs)}")

    print(f"\n{'═'*75}")
    print(f"  DONE. Total configurations tested: {len(results)} ({len(valid)} succeeded, {len(results)-len(valid)} failed)")
    print(f"{'═'*75}")


if __name__ == "__main__":
    main()
