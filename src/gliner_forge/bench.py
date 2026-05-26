"""Unified benchmark CLI for GLiNER-Forge.

Usage:
    python -m gliner_forge.bench --model small-v2.5 --backend onnx --threshold 0.3
    python -m gliner_forge.bench --all
"""
from __future__ import annotations

import argparse
import time
from collections import defaultdict
from pathlib import Path

MODEL_MAP = {
    "small-v2.5": "gliner-community/gliner_small-v2.5",
    "medium-v2.5": "gliner-community/gliner_medium-v2.5",
    "large-v2.5": "gliner-community/gliner_large-v2.5",
    "x-small": "knowledgator/gliner-x-small",
    "x-base": "knowledgator/gliner-x-base",
    "x-large": "knowledgator/gliner-x-large",
}

LANGS = ['ar', 'en', 'es', 'fr', 'ja', 'ko', 'ru', 'th', 'vi', 'zh-TW']


def load_test_data():
    """Load test cases from bench/test_data_taiwan.py."""
    import importlib.util
    bench_dir = Path(__file__).parent.parent.parent / "bench"
    spec = importlib.util.spec_from_file_location("test_data", bench_dir / "test_data_taiwan.py")
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod.TEST_CASES


def evaluate(predict_fn, test_cases, threshold=0.3):
    """Run evaluation, return (recall%, ms/call, per_lang_dict)."""
    lr = defaultdict(lambda: {"f": 0, "t": 0})
    times = []
    for tc in test_cases:
        t0 = time.perf_counter()
        preds = predict_fn(tc["text"], tc["labels"], threshold)
        times.append(time.perf_counter() - t0)
        for e in tc["expected"]:
            ok = any(
                (e["text"].lower() in p["text"].lower() or p["text"].lower() in e["text"].lower())
                and e["label"] == p["label"]
                for p in preds
            )
            lr[tc["lang"]]["t"] += 1
            if ok:
                lr[tc["lang"]]["f"] += 1
    tf = sum(v["f"] for v in lr.values())
    tt = sum(v["t"] for v in lr.values())
    return tf / tt * 100 if tt else 0, sum(times) / len(times) * 1000, lr


def run_one(model_name: str, backend: str, threshold: float, test_cases):
    """Run a single benchmark configuration."""
    repo = MODEL_MAP.get(model_name, model_name)

    if backend == "onnx-standalone":
        from gliner_forge.onnx_infer import GLiNERStandalone
        model_dir = Path(__file__).parent.parent.parent / "models" / model_name
        m = GLiNERStandalone(str(model_dir))
        predict_fn = lambda text, labels, th: m.predict_entities(text, labels, th)
    else:
        from gliner import GLiNER
        m = GLiNER.from_pretrained(repo, load_onnx_model=(backend == "onnx"))
        if backend == "mps":
            m.to("mps")
        predict_fn = lambda text, labels, th: m.predict_entities(text, labels, threshold=th)

    # Warmup
    for tc in test_cases[:2]:
        predict_fn(tc["text"], tc["labels"], threshold)

    recall, ms, lr = evaluate(predict_fn, test_cases, threshold)
    return recall, ms, lr


def print_row(model, backend, recall, ms, lr):
    cols = ""
    for lang in LANGS:
        if lang in lr and lr[lang]["t"] > 0:
            cols += f"{lr[lang]['f'] * 100 // lr[lang]['t']:<5}"
        else:
            cols += f"{'--':<5}"
    print(f"{model:<15}{backend:<18}{recall:<9.1f}{ms:<9.1f}{cols}")


def main():
    parser = argparse.ArgumentParser(description="GLiNER-Forge Benchmark")
    parser.add_argument("--model", choices=list(MODEL_MAP.keys()), default="small-v2.5")
    parser.add_argument("--backend", choices=["cpu", "mps", "onnx", "onnx-standalone"], default="cpu")
    parser.add_argument("--threshold", type=float, default=0.3)
    parser.add_argument("--all", action="store_true", help="Run all models × backends")
    args = parser.parse_args()

    test_cases = load_test_data()

    hdr = f"{'Model':<15}{'Backend':<18}{'Recall%':<9}{'ms/call':<9}" + "".join(f"{l:<5}" for l in LANGS)
    print(hdr)
    print("-" * len(hdr))

    if args.all:
        configs = [
            ("small-v2.5", "cpu"), ("small-v2.5", "onnx"), ("small-v2.5", "onnx-standalone"),
            ("medium-v2.5", "cpu"), ("medium-v2.5", "onnx"),
            ("large-v2.5", "cpu"), ("large-v2.5", "onnx"),
            ("x-small", "cpu"), ("x-base", "cpu"), ("x-large", "cpu"),
        ]
        for model, backend in configs:
            try:
                recall, ms, lr = run_one(model, backend, args.threshold, test_cases)
                print_row(model, backend, recall, ms, lr)
            except Exception as e:
                print(f"{model:<15}{backend:<18}FAIL: {e}")
    else:
        recall, ms, lr = run_one(args.model, args.backend, args.threshold, test_cases)
        print_row(args.model, args.backend, recall, ms, lr)


if __name__ == "__main__":
    main()
