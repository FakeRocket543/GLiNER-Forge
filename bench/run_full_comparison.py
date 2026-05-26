"""Full GLiNER benchmark: compare models × backends on Taiwan NER test data."""
import sys
import time
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from test_data_taiwan import TEST_CASES

MODELS = [
    ("gliner-community/gliner_small-v2.5", "small", "~100MB"),
    ("gliner-community/gliner_medium-v2.5", "medium", "~200MB"),
    ("gliner-community/gliner_large-v2.5", "large", "~400MB"),
]

WARMUP = 3
TIMED = 5


def fuzzy_match(expected, predicted):
    return (expected["label"] == predicted.get("label", predicted.get("type", "")) and
            (expected["text"] in predicted.get("text", predicted.get("span", "")) or
             predicted.get("text", predicted.get("span", "")) in expected["text"]))


def compute_recall(model, predict_fn):
    """Compute overall recall across all TEST_CASES."""
    found = total = 0
    for case in TEST_CASES:
        entities = predict_fn(model, case["text"], case["labels"])
        for exp in case["expected"]:
            if any(fuzzy_match(exp, pred) for pred in entities):
                found += 1
            total += 1
    return found / total if total else 0.0


def measure_time(model, predict_fn):
    """Run warmup + timed iterations, return avg ms/call."""
    for _ in range(WARMUP):
        for case in TEST_CASES:
            predict_fn(model, case["text"], case["labels"])

    start = time.perf_counter()
    for _ in range(TIMED):
        for case in TEST_CASES:
            predict_fn(model, case["text"], case["labels"])
    elapsed = time.perf_counter() - start

    calls = TIMED * len(TEST_CASES)
    return (elapsed / calls) * 1000


def gliner_predict(model, text, labels):
    return model.predict_entities(text, labels, threshold=0.3)


def mlx_predict(pipe, text, labels):
    from gliner_mlx.infer import predict
    result = predict(pipe, text, labels, relations=[])
    return result.get("entities", [])


def bench_gliner(name, size_label, size_str, onnx=False):
    """Benchmark a GLiNER model with transformer or ONNX backend."""
    backend = "ONNX" if onnx else "Transformer"
    quantized = "Yes (dyn)" if onnx else "No"
    print(f"  Loading {name} [{backend}]...", flush=True)

    from gliner import GLiNER
    if onnx:
        model = GLiNER.from_pretrained(name, load_onnx_model=True)
    else:
        model = GLiNER.from_pretrained(name)

    recall = compute_recall(model, gliner_predict)
    avg_ms = measure_time(model, gliner_predict)

    del model
    return {
        "model": name.split("/")[-1],
        "size": size_str,
        "backend": backend,
        "quantized": quantized,
        "recall": recall * 100,
        "avg_ms": avg_ms,
    }


def bench_mlx():
    """Benchmark MLX backend via openmed."""
    print("  Loading OpenMed/gliner-relex-base-v1.0-mlx [MLX]...", flush=True)

    from gliner_mlx.infer import load_model
    pipe = load_model()

    recall = compute_recall(pipe, mlx_predict)
    avg_ms = measure_time(pipe, mlx_predict)

    del pipe
    return {
        "model": "gliner-relex-base-v1.0-mlx",
        "size": "~200MB",
        "backend": "MLX",
        "quantized": "No",
        "recall": recall * 100,
        "avg_ms": avg_ms,
    }


def print_table(results):
    header = f"{'Model':<32} {'Size':<8} {'Backend':<13} {'Quantized':<10} {'Recall%':<9} {'Avg ms/call'}"
    sep = "-" * len(header)
    print(f"\n{'='*len(header)}")
    print("FINAL COMPARISON")
    print(f"{'='*len(header)}")
    print(header)
    print(sep)
    for r in results:
        print(f"{r['model']:<32} {r['size']:<8} {r['backend']:<13} {r['quantized']:<10} {r['recall']:<9.1f} {r['avg_ms']:.1f}")
    print(sep)


def main():
    print(f"GLiNER Full Benchmark — {len(TEST_CASES)} test cases, {WARMUP} warmup + {TIMED} timed iterations\n")
    results = []

    # GLiNER models × backends
    for name, size_label, size_str in MODELS:
        for onnx in [False, True]:
            try:
                r = bench_gliner(name, size_label, size_str, onnx=onnx)
                results.append(r)
                print(f"    → Recall={r['recall']:.1f}%  Avg={r['avg_ms']:.1f}ms/call")
            except Exception as e:
                backend = "ONNX" if onnx else "Transformer"
                print(f"    ✗ FAILED ({backend}): {e}")

    # MLX backend
    try:
        r = bench_mlx()
        results.append(r)
        print(f"    → Recall={r['recall']:.1f}%  Avg={r['avg_ms']:.1f}ms/call")
    except Exception as e:
        print(f"    ✗ FAILED (MLX): {e}")

    print_table(results)


if __name__ == "__main__":
    main()
