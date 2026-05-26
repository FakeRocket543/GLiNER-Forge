"""
GLiNER ONNX — RK3588S (NanoPi M6) Benchmark

Platform: NanoPi M6 (RK3588S, 4×A55 + 4×A76, 32GB LPDDR4x)
OS: Armbian / Linux 6.1
Runtime: ONNX Runtime 1.26.0, CPUExecutionProvider (ARM NEON)
Model: SemplificaAI/gliner2-multi-v1-onnx (mDeBERTa-v3-base, 12 layers, 768 dim)

Usage:
    python bench_rk3588s.py --variant fp16|int8|fp32

Requirements:
    pip install onnxruntime tokenizers numpy
"""

import argparse
import os
import time
from dataclasses import dataclass, field

import numpy as np
import onnxruntime as ort
from tokenizers import Tokenizer

# ── Model paths ──────────────────────────────────────────────

MODEL_BASE = os.environ.get("GLINER_MODEL_DIR", os.path.expanduser("~/gliner-model"))
TOKENIZER_PATH = os.path.join(MODEL_BASE, "fp16", "tokenizer.json")

VARIANTS = {
    "fp16": {
        "encoder": os.path.join(MODEL_BASE, "fp16", "encoder_fp16.onnx"),
        "span_rep": os.path.join(MODEL_BASE, "fp16", "span_rep_fp16.onnx"),
        "classifier": os.path.join(MODEL_BASE, "fp16", "classifier_fp16.onnx"),
    },
    "fp32": {
        "encoder": os.path.join(MODEL_BASE, "fp32", "encoder_fp32_full.onnx"),
    },
    "int8": {
        "encoder": os.path.join(MODEL_BASE, "int8", "encoder_int8.onnx"),
        "span_rep": os.path.join(MODEL_BASE, "int8", "span_rep_int8.onnx"),
        "classifier": os.path.join(MODEL_BASE, "int8", "classifier_int8.onnx"),
    },
}

# ── Test data from inff.cc ───────────────────────────────────

TEST_TEXTS = [
    {
        "name": "德國民防 (zh-TW, 124 tok)",
        "text": "德國最新民調顯示，72%受訪者對聯邦國防軍的防衛準備能力存疑。德國之聲（DW）報導，此次民調同時顯示，2025年德國取得護照人數創歷史新高。俄羅斯總統普丁與巴林國王哈瑪德·本·伊薩·阿勒哈里法通電話，雙方強調需快速解決伊朗周邊危機。",
        "labels": ["person", "organization", "country", "location", "date", "percentage"],
    },
    {
        "name": "馬德里示威 (zh-TW, 65 tok)",
        "text": "馬德里爆發大規模示威，數萬民眾要求首相桑切斯下台。根據組織方的估計，此次集會有12萬人參加。",
        "labels": ["person", "city", "country", "event", "number of people"],
    },
    {
        "name": "中東衝突 (zh-TW, 92 tok)",
        "text": "法國外交部表示，本-格維爾因發布影片，顯示以色列軍方對加沙之船支持者進行羞辱性對待，因此禁止入境。烏克蘭武裝部隊無人機襲擊俄佔盧甘斯克人民共和國學校，造成21人死亡。",
        "labels": ["person", "country", "organization", "location", "number of casualties"],
    },
    {
        "name": "English short (27 tok)",
        "text": "Tim Cook is the CEO of Apple Inc., based in Cupertino, California.",
        "labels": ["person", "organization", "location"],
    },
]


@dataclass
class BenchResult:
    variant: str
    text_name: str
    tokens: int = 0
    encoder_ms: float = 0.0
    load_ms: float = 0.0
    model_mb: float = 0.0
    hidden_shape: tuple = ()
    runs: int = 5


def build_gliner_input(text: str, labels: list[str], tokenizer, max_len: int = 512):
    """Build GLiNER-style input: [P] entities ( [E] label1 [E] label2 ) [SEP_TEXT] text"""
    schema = " ".join(f"[E] {l}" for l in labels)
    full_input = f"[P] entities ( {schema} ) [SEP_TEXT] {text}"
    encoded = tokenizer.encode(full_input)
    ids = encoded.ids
    mask = encoded.attention_mask
    pad_len = max_len - len(ids)
    ids = ids + [0] * pad_len
    mask = mask + [0] * pad_len
    return np.array([ids], dtype=np.int64), sum(mask)


def bench_encoder(encoder, input_ids: np.ndarray, runs: int = 5) -> float:
    """Benchmark encoder, returns average ms."""
    encoder.run(None, {"input_ids": input_ids})  # warmup
    times = []
    for _ in range(runs):
        t0 = time.time()
        encoder.run(None, {"input_ids": input_ids})
        times.append(time.time() - t0)
    return float(np.mean(times) * 1000)


def main():
    parser = argparse.ArgumentParser(description="GLiNER ONNX benchmark on RK3588S")
    parser.add_argument("--variant", choices=list(VARIANTS.keys()), nargs="+",
                        default=["fp16", "int8"], help="Variants to benchmark")
    parser.add_argument("--runs", type=int, default=5, help="Runs per test (default: 5)")
    parser.add_argument("--all", action="store_true", help="Benchmark all variants")
    args = parser.parse_args()

    if args.all:
        args.variant = list(VARIANTS.keys())

    tokenizer = Tokenizer.from_file(TOKENIZER_PATH)
    results: list[BenchResult] = []

    for variant in args.variant:
        paths = VARIANTS[variant]
        enc_path = paths["encoder"]
        if not os.path.exists(enc_path):
            print(f"⚠️  Skipping {variant}: {enc_path} not found")
            continue

        print(f"\n{'='*60}")
        model_mb = os.path.getsize(enc_path) / 1024 / 1024
        print(f"📦 {variant.upper()} encoder: {model_mb:.0f}MB")

        t0 = time.time()
        opts = ort.SessionOptions()
        opts.graph_optimization_level = ort.GraphOptimizationLevel.ORT_ENABLE_ALL
        encoder = ort.InferenceSession(enc_path, opts, providers=["CPUExecutionProvider"])
        load_ms = (time.time() - t0) * 1000
        print(f"   Loaded in {load_ms:.0f}ms")

        for test in TEST_TEXTS:
            input_ids, n_tokens = build_gliner_input(test["text"], test["labels"], tokenizer)
            avg_ms = bench_encoder(encoder, input_ids, runs=args.runs)
            r = BenchResult(
                variant=variant, text_name=test["name"], tokens=n_tokens,
                encoder_ms=avg_ms, load_ms=load_ms, model_mb=model_mb,
                hidden_shape=(1, 512, 768), runs=args.runs,
            )
            results.append(r)
            print(f"   {test['name']}: {avg_ms:.0f}ms ({n_tokens} tok)")

    # Summary
    print(f"\n{'='*60}")
    print("📊 RK3588S Benchmark Summary")
    print(f"{'='*60}")
    print(f"{'Variant':<8} {'Size':>6} {'Long':>8} {'Short':>8} {'EN':>8} {'Speedup':>8}")
    print(f"{'-'*8} {'-'*6} {'-'*8} {'-'*8} {'-'*8} {'-'*8}")

    baseline = None
    for variant in args.variant:
        vresults = [r for r in results if r.variant == variant]
        if not vresults:
            continue
        long_ms = next((r.encoder_ms for r in vresults if "124 tok" in r.text_name), 0)
        short_ms = next((r.encoder_ms for r in vresults if "65 tok" in r.text_name), 0)
        en_ms = next((r.encoder_ms for r in vresults if "English" in r.text_name), 0)
        size_mb = vresults[0].model_mb

        if baseline is None:
            baseline = long_ms
            speedup = "1.00x"
        else:
            speedup = f"{baseline/long_ms:.2f}x"

        print(f"{variant:<8} {size_mb:>5.0f}MB {long_ms:>7.0f}ms {short_ms:>7.0f}ms {en_ms:>7.0f}ms {speedup:>8}")

    print(f"\nPlatform: NanoPi M6 (RK3588S, aarch64, 32GB RAM)")
    print(f"Runtime: ORT {ort.__version__}, CPUExecutionProvider, pad=512")


if __name__ == "__main__":
    main()
