"""Benchmark GLiNER models: PyTorch vs ONNX FP32 vs ONNX INT8."""
import sys, os, time, glob
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from bench.test_data_taiwan import TEST_CASES

from gliner import GLiNER
from onnxruntime.quantization import quantize_dynamic, QuantType

MODELS = [
    ("gliner-community/gliner_small-v2.5", "small-v2.5"),
    ("gliner-community/gliner_medium-v2.5", "medium-v2.5"),
]
WARMUP, RUNS = 2, 3
THRESHOLD = 0.3


def fuzzy_match(pred_ents, expected):
    """Recall with fuzzy matching: substring in either direction + label match."""
    hits = 0
    for exp in expected:
        for p in pred_ents:
            if p["label"] == exp["label"] and (exp["text"] in p["text"] or p["text"] in exp["text"]):
                hits += 1
                break
    return hits / len(expected) if expected else 1.0


def benchmark(model, label):
    """Run benchmark: 2 warmup + 3 timed, return avg time and recall."""
    all_labels_set = set()
    for tc in TEST_CASES:
        all_labels_set.update(tc["labels"])

    # Warmup
    for _ in range(WARMUP):
        for tc in TEST_CASES:
            model.predict_entities(tc["text"], tc["labels"], threshold=THRESHOLD)

    # Timed
    total_time = 0
    recalls = []
    for _ in range(RUNS):
        t0 = time.perf_counter()
        for tc in TEST_CASES:
            preds = model.predict_entities(tc["text"], tc["labels"], threshold=THRESHOLD)
        total_time += time.perf_counter() - t0

    # Compute recall on last run
    for tc in TEST_CASES:
        preds = model.predict_entities(tc["text"], tc["labels"], threshold=THRESHOLD)
        recalls.append(fuzzy_match(preds, tc["expected"]))

    avg_time = total_time / RUNS
    avg_recall = sum(recalls) / len(recalls)
    return avg_time, avg_recall


def main():
    results = []

    for model_name, short_name in MODELS:
        print(f"\n{'='*60}")
        print(f"Model: {model_name}")
        print(f"{'='*60}")

        # --- PyTorch ---
        print(f"\n[PyTorch] Loading {model_name}...")
        model_pt = GLiNER.from_pretrained(model_name)
        model_pt.eval()
        pt_time, pt_recall = benchmark(model_pt, f"{short_name}/pytorch")
        results.append((short_name, "PyTorch", pt_time, pt_recall))
        print(f"  Time: {pt_time:.3f}s | Recall: {pt_recall:.1%}")

        # --- ONNX Export ---
        save_dir = Path(f"models/onnx/{short_name}")
        onnx_path = save_dir / "model.onnx"
        quant_path = save_dir / "model_quantized.onnx"

        if not onnx_path.exists():
            print(f"\n[ONNX] Exporting to {save_dir}...")
            try:
                export_result = model_pt.export_to_onnx(
                    save_dir=str(save_dir),
                    quantize=True,
                )
                print(f"  Export result: {export_result}")
            except Exception as e:
                print(f"  Export failed: {e}")
                # Try manual quantization if export succeeded but quantize failed
                if onnx_path.exists():
                    print("  ONNX file exists, trying manual quantization...")
        else:
            print(f"\n[ONNX] Already exported at {save_dir}")

        # Manual quantization fallback
        if onnx_path.exists() and not quant_path.exists():
            print("  Running manual INT8 quantization...")
            try:
                quantize_dynamic(str(onnx_path), str(quant_path), weight_type=QuantType.QInt8)
                print(f"  Quantized: {quant_path}")
            except Exception as e:
                print(f"  Quantization failed: {e}")

        # --- ONNX FP32 Benchmark ---
        if onnx_path.exists():
            print(f"\n[ONNX FP32] Loading from {save_dir}...")
            try:
                model_onnx = GLiNER.from_pretrained(str(save_dir), load_onnx_model=True)
                onnx_time, onnx_recall = benchmark(model_onnx, f"{short_name}/onnx-fp32")
                results.append((short_name, "ONNX FP32", onnx_time, onnx_recall))
                print(f"  Time: {onnx_time:.3f}s | Recall: {onnx_recall:.1%}")
            except Exception as e:
                print(f"  ONNX FP32 load/bench failed: {e}")

        # --- ONNX INT8 Benchmark ---
        if quant_path.exists():
            print(f"\n[ONNX INT8] Loading from {save_dir}...")
            try:
                model_int8 = GLiNER.from_pretrained(
                    str(save_dir), load_onnx_model=True, onnx_model_file="model_quantized.onnx"
                )
                int8_time, int8_recall = benchmark(model_int8, f"{short_name}/onnx-int8")
                results.append((short_name, "ONNX INT8", int8_time, int8_recall))
                print(f"  Time: {int8_time:.3f}s | Recall: {int8_recall:.1%}")
            except Exception as e:
                print(f"  ONNX INT8 load/bench failed: {e}")

        # Free memory
        del model_pt

    # --- Final Table ---
    print(f"\n\n{'='*70}")
    print(f"{'FINAL RESULTS':^70}")
    print(f"{'='*70}")
    print(f"{'Model':<15} {'Variant':<12} {'Time (s)':<12} {'Recall':<10} {'Speedup':<10}")
    print(f"{'-'*15} {'-'*12} {'-'*12} {'-'*10} {'-'*10}")

    # Group by model for speedup calculation
    by_model = {}
    for short, variant, t, r in results:
        by_model.setdefault(short, []).append((variant, t, r))

    for short, variants in by_model.items():
        pt_time_ref = next((t for v, t, r in variants if v == "PyTorch"), None)
        for variant, t, r in variants:
            speedup = f"{pt_time_ref/t:.2f}x" if pt_time_ref else "N/A"
            print(f"{short:<15} {variant:<12} {t:<12.3f} {r:<10.1%} {speedup:<10}")

    print(f"{'='*70}")
    print(f"\nTest cases: {len(TEST_CASES)} | Warmup: {WARMUP} | Timed runs: {RUNS}")


if __name__ == "__main__":
    main()
