"""Benchmark all GLiNER model sizes × backends (CPU, MPS, ONNX)."""
import sys, os, time
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from bench.test_data_taiwan import TEST_CASES
import torch
from gliner import GLiNER

MODELS = [
    ("small-v2.5", "gliner-community/gliner_small-v2.5"),
    ("medium-v2.5", "gliner-community/gliner_medium-v2.5"),
    ("large-v2.5", "gliner-community/gliner_large-v2.5"),
]
BACKENDS = ["CPU FP32", "MPS FP32", "ONNX FP32"]
WARMUP, TIMED = 2, 3
THRESHOLD = 0.3

# Language mapping
LANG_ORDER = ["ar", "en", "es", "fr", "ja", "ko", "ru", "th", "vi", "zh"]
def get_lang(tc):
    l = tc["lang"]
    if l.startswith("zh"): return "zh"
    return l

def fuzzy_match(pred, exp):
    """Substring + label match."""
    return (pred["label"] == exp["label"] and
            (exp["text"] in pred["text"] or pred["text"] in exp["text"]))

def calc_recall(predictions_per_case):
    """Return overall recall and per-language recall dict."""
    lang_hits, lang_total = {}, {}
    for tc, preds in predictions_per_case:
        lang = get_lang(tc)
        lang_total.setdefault(lang, 0)
        lang_hits.setdefault(lang, 0)
        for exp in tc["expected"]:
            lang_total[lang] += 1
            if any(fuzzy_match(p, exp) for p in preds):
                lang_hits[lang] += 1
    total = sum(lang_total.values())
    hits = sum(lang_hits.values())
    overall = hits / total * 100 if total else 0
    per_lang = {l: (lang_hits.get(l,0) / lang_total[l] * 100 if lang_total.get(l) else 0) for l in LANG_ORDER}
    return overall, per_lang

def run_inference(model, test_cases):
    """Run all test cases, return list of (tc, preds)."""
    results = []
    for tc in test_cases:
        preds = model.predict_entities(tc["text"], tc["labels"], threshold=THRESHOLD)
        results.append((tc, preds))
    return results

def bench_model(model, test_cases):
    """Warmup + timed runs. Return (recall%, per_lang, ms_per_call, total_s)."""
    # Warmup
    for _ in range(WARMUP):
        run_inference(model, test_cases)
    # Timed
    times = []
    last_results = None
    for _ in range(TIMED):
        t0 = time.perf_counter()
        last_results = run_inference(model, test_cases)
        times.append(time.perf_counter() - t0)
    avg_total = sum(times) / len(times)
    ms_per_call = avg_total / len(test_cases) * 1000
    overall, per_lang = calc_recall(last_results)
    return overall, per_lang, ms_per_call, avg_total

def cleanup():
    if torch.backends.mps.is_available():
        torch.mps.empty_cache()
    import gc; gc.collect()

results = []

for size_name, model_id in MODELS:
    print(f"\n{'='*60}")
    print(f"Loading {model_id}...")
    print(f"{'='*60}")

    # --- CPU FP32 ---
    try:
        print(f"  [{size_name}] CPU FP32...")
        model = GLiNER.from_pretrained(model_id)
        r = bench_model(model, TEST_CASES)
        results.append((size_name, "CPU FP32", *r))
        print(f"    Recall={r[0]:.1f}% ms/call={r[2]:.1f}")
    except Exception as e:
        print(f"    FAILED: {e}")
        results.append((size_name, "CPU FP32", 0, {}, 0, 0))
        model = None

    # --- MPS FP32 ---
    try:
        print(f"  [{size_name}] MPS FP32...")
        if model is None:
            model = GLiNER.from_pretrained(model_id)
        model = model.to("mps")
        r = bench_model(model, TEST_CASES)
        results.append((size_name, "MPS FP32", *r))
        print(f"    Recall={r[0]:.1f}% ms/call={r[2]:.1f}")
    except Exception as e:
        print(f"    FAILED (MPS): {e}")
        results.append((size_name, "MPS FP32", 0, {}, 0, 0))

    # Cleanup before ONNX
    del model
    cleanup()

    # --- ONNX FP32 ---
    try:
        print(f"  [{size_name}] ONNX FP32...")
        save_dir = os.path.expanduser(f"~/projets/GLiNER/models/{size_name}")
        os.makedirs(save_dir, exist_ok=True)
        onnx_path = os.path.join(save_dir, "model.onnx")
        if not os.path.exists(onnx_path):
            model = GLiNER.from_pretrained(model_id)
            model.to("cpu")
            model.export_to_onnx(save_dir)
            del model
            cleanup()
        # Reload with ONNX
        model = GLiNER.from_pretrained(save_dir, load_onnx_model=True)
        r = bench_model(model, TEST_CASES)
        results.append((size_name, "ONNX FP32", *r))
        print(f"    Recall={r[0]:.1f}% ms/call={r[2]:.1f}")
        del model
        cleanup()
    except Exception as e:
        print(f"    FAILED (ONNX): {e}")
        results.append((size_name, "ONNX FP32", 0, {}, 0, 0))
        try: del model
        except: pass
        cleanup()

# --- Print final table ---
print(f"\n\n{'='*60}")
print("=== FULL SIZE COMPARISON ===")
lang_hdr = "  ".join(f"{l:>3}" for l in LANG_ORDER)
header = f"{'Model':<14} {'Backend':<10} {'Recall%':>7} {'ms/call':>7} {'Total(s)':>8}  {lang_hdr}"
print(header)
print("─" * len(header))

for row in results:
    size_name, backend, recall, per_lang, ms_call, total_s = row
    if isinstance(per_lang, dict):
        lang_vals = "  ".join(f"{per_lang.get(l,0):>3.0f}" for l in LANG_ORDER)
    else:
        lang_vals = "  ".join(f"{'–':>3}" for _ in LANG_ORDER)
    print(f"{size_name:<14} {backend:<10} {recall:>6.1f}% {ms_call:>7.1f} {total_s:>8.2f}  {lang_vals}")

print()
