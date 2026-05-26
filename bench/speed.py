"""Benchmark: compare GLiNER inference speed across backends."""
import sys
import time
import json
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "python"))

TEST_TEXTS = [
    "Tim Cook is the CEO of Apple Inc., headquartered in Cupertino, California.",
    "Elon Musk founded SpaceX and leads Tesla in Austin, Texas.",
    "台積電董事長魏哲家宣布在高雄設立新廠。",
]
TEST_LABELS = ["person", "organization", "location"]
TEST_RELATIONS = ["works at", "headquartered in", "founded"]
N_WARMUP = 3
N_ITER = 20


def bench_openmed_mlx():
    from gliner_mlx.infer import load_model, predict
    pipe = load_model()
    # warmup
    for _ in range(N_WARMUP):
        for t in TEST_TEXTS:
            predict(pipe, t, TEST_LABELS, TEST_RELATIONS)
    # timed
    start = time.perf_counter()
    for _ in range(N_ITER):
        for t in TEST_TEXTS:
            predict(pipe, t, TEST_LABELS, TEST_RELATIONS)
    elapsed = time.perf_counter() - start
    total = N_ITER * len(TEST_TEXTS)
    return {"backend": "MLX (OpenMed)", "total_ms": elapsed * 1000, "avg_ms": elapsed * 1000 / total}


def bench_gliner_pytorch():
    from gliner import GLiNER
    model = GLiNER.from_pretrained("urchade/gliner_medium-v2.1")
    # warmup
    for _ in range(N_WARMUP):
        for t in TEST_TEXTS:
            model.predict_entities(t, TEST_LABELS)
    # timed
    start = time.perf_counter()
    for _ in range(N_ITER):
        for t in TEST_TEXTS:
            model.predict_entities(t, TEST_LABELS)
    elapsed = time.perf_counter() - start
    total = N_ITER * len(TEST_TEXTS)
    return {"backend": "PyTorch (CPU)", "total_ms": elapsed * 1000, "avg_ms": elapsed * 1000 / total}


if __name__ == "__main__":
    results = []
    print("=== GLiNER Speed Benchmark ===\n")

    try:
        r = bench_gliner_pytorch()
        results.append(r)
        print(f"  {r['backend']:20s}: {r['avg_ms']:.1f} ms/call")
    except Exception as e:
        print(f"  PyTorch: SKIP ({e})")

    try:
        r = bench_openmed_mlx()
        results.append(r)
        print(f"  {r['backend']:20s}: {r['avg_ms']:.1f} ms/call")
    except Exception as e:
        print(f"  MLX: SKIP ({e})")

    print(f"\n{N_ITER} iterations × {len(TEST_TEXTS)} texts each")
    Path("bench/results.json").write_text(json.dumps(results, indent=2))
