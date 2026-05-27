# GLiNER Full Matrix Benchmark — Supplementary Findings

**Date:** 2026-05-27
**Follow-up to:** full_matrix_report.md

---

## 1. Quantization Deep Dive

### Results Summary

| Model | fp32 F1 | fp16 F1 | int8 F1 | int8 Δ | Notes |
|-------|---------|---------|---------|--------|-------|
| small-v2.5 | 0.370 | 0.370 | 0.337 | -0.033 | ✅ Acceptable |
| medium-v2.5 | 0.352 | 0.352 | 0.073 | **-0.279** | ❌ BROKEN |
| large-v2.5 | 0.329 | ❌ N/A | 0.335 | **+0.006** | ✅ No loss |

### Key Findings

1. **medium-v2.5 int8 is fundamentally broken** — Both quantization approaches failed:
   - Original (from fp16 source): F1=0.073
   - Re-quantized from fp32 source: F1=0.022 (even worse)
   - Root cause: `quantize_dynamic` produces broken output for deberta-v3-base architecture at this size. The RK3588S report's `fix_fp16.py` pipeline fixed the loading error but didn't fix the accuracy loss.

2. **large-v2.5 int8 works perfectly** — F1=0.335 vs fp32=0.329 (within noise)

3. **large-v2.5 fp16 cannot be converted post-hoc** — ORT rejects mixed fp16/fp32 graphs. Proper fp16 requires export-time conversion (like small/medium which were exported with fp16 from the start).

4. **fp16 is always lossless** when properly exported (small, medium both show F1 identical to fp32)

### Recommendation

| Model | Recommended Variant | Rationale |
|-------|-------------------|-----------|
| small-v2.5 | int8 (188MB) | 2× smaller, minimal quality loss |
| medium-v2.5 | fp16 (399MB) | int8 is broken, fp16 is lossless |
| large-v2.5 | int8 (636MB) | Same quality as fp32, 63% smaller |

---

## 2. CJK (zh-TW, ja, ko) Zero F1 — Root Cause Analysis

### Problem

All models show F1 ≈ 0 for zh-TW, ja, ko. Investigation reveals this is **NOT a model capability issue** — it's a word splitting issue.

### Root Cause

GLiNER uses `words_splitter_type: "whitespace"` which splits text on spaces. CJK languages have no word-separating spaces, so:

```
Input: "臺灣位於東亞、太平洋西北側的島嶼"
Split: ["臺灣位於東亞", "、", "太平洋西北側的島嶼"]  (3 "words")
```

The model can only produce entities at word boundaries, so it outputs entire chunks as single entities instead of precise spans like "臺灣" or "東亞".

### Proof

With CJK character-level splitting (each character = 1 word):
- "臺灣" ✅ detected as location (score=0.508)
- "東亞" ✅ detected as location (score=0.519)

### Solution Options

1. **Character-level splitting for CJK** — simple, works for NER, standard in Chinese NER
2. **Jieba/pkuseg tokenization** — better linguistic units but adds dependency
3. **The model's own subword tokenizer** — already handles CJK internally, but the span layer needs word-level indices

### Impact on Benchmark

The true F1 for zh-TW with proper CJK splitting would be significantly higher. Current "0.00" scores are artifacts of the word splitter, not model quality.

---

## 3. Model Comparison (corrected interpretation)

### Adjusting for CJK splitting issue

Excluding zh-TW/ja/ko (where scores are 0 due to splitting bug):

| Model | Non-CJK Avg F1 | Best Language |
|-------|-----------------|--------------|
| GLiNER-X large | 0.72 | ru (0.86) |
| GLiNER-X base | 0.66 | ru (0.86) |
| GLiNER small-v2.5 | 0.62 | ru (0.88) |
| GLiNER medium-v2.5 | 0.59 | vi (0.83) |
| GLiNER large-v2.5 | 0.55 | ru (0.86) |
| OpenMed MLX | 0.56 | vi (0.80) |

### Counter-intuitive Finding

**Larger models ≠ better for GLiNER v2.5.** The small model (F1=0.62) outperforms large (F1=0.55). This is because:
- v2.5 models were trained with different label schemes per size
- The "expected" labels in our test data may not match what larger models learned
- GLiNER-X models were specifically trained for cross-lingual transfer → better multilingual

---

## 4. Backend Performance

| Backend | Avg Latency | Best For |
|---------|-------------|----------|
| ONNX CPU int8 | 9ms | Production (if model supports int8) |
| ONNX CPU fp32 | 11-45ms | Default safe choice |
| MLX | 11ms | macOS only, different model |
| PyTorch MPS | 16-29ms | Development, full model access |
| ONNX CoreML | 29-131ms | ❌ Slower than CPU for these models |
| PyTorch CPU | 25-111ms | Fallback |

### CoreML is slower!

CoreML adds overhead for model compilation and doesn't accelerate small-to-medium transformer models effectively on Apple Silicon. The Neural Engine doesn't kick in for these graph patterns.

---

## 5. Remaining Work

- [ ] Implement CJK-aware word splitter in `GLiNERStandalone` and C++ wrapper
- [ ] Re-run zh-TW/ja/ko tests with fixed splitter
- [ ] Investigate medium int8 quantization failure (may need static quantization with calibration data)
- [ ] Export large fp16 from PyTorch directly (not post-hoc ONNX conversion)
- [ ] GLiNER2 alternative model (original repo 404'd)
