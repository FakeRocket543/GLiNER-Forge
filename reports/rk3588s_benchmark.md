# GLiNER ONNX — RK3588S (NanoPi M6) Benchmark Report

**Date:** 2026-05-26
**Platform:** NanoPi M6 (Rockchip RK3588S)
**CPU:** 4× Cortex-A76 @ 2.4GHz + 4× Cortex-A55 @ 1.8GHz
**RAM:** 32GB LPDDR4x
**OS:** Armbian (Linux 6.1.118, aarch64)
**Runtime:** ONNX Runtime 1.26.0, CPUExecutionProvider (ARM NEON)
**Model:** `SemplificaAI/gliner2-multi-v1-onnx` (mDeBERTa-v3-base, 12-layer, 768-dim, 110M params)

---

## Executive Summary

GLiNER (zero-shot NER) runs successfully on RK3588S with INT8 quantization achieving **2.2× speedup** over FP16 baseline, at **~850ms per 512-token encoder pass**. The fp16→int8 conversion required a non-trivial fp16 cleanup step due to hidden fp16 tensors in the ONNX graph.

---

## Benchmark Results

### Encoder Speed (512-token padded sequence)

| Variant | Size | zh-TW Long (124 tok) | zh-TW Short (65 tok) | EN (27 tok) | Speedup |
|---------|------|---------------------|---------------------|-------------|---------|
| **fp16** | 531MB | 1878ms | 1875ms | 1868ms | 1.00× |
| **int8** | 322MB | 853ms | 842ms | 840ms | **2.20×** |
| **fp32** | 1060MB | ~3600ms (est.) | — | — | ~0.5× |

> All times are avg of 5 runs after warmup. Input padded to 512 tokens regardless of actual length.

### Model Size Comparison

| Component | fp16 | int8 | Reduction |
|-----------|------|------|-----------|
| encoder | 531MB | 322MB | -39% |
| span_rep | 32MB | 16MB | -50% |
| classifier | 2.3MB | 1.2MB | -48% |
| **Total** | **565MB** | **339MB** | **-40%** |

### Load Time

| Variant | Load Time |
|---------|-----------|
| fp16 | 3.7s |
| int8 | 3.0s |

---

## Quantization Pipeline

### The fp16→int8 Pitfall

The source ONNX model (fp16) cannot be directly quantized to int8 using `onnxruntime.quantization.quantize_dynamic`. Three categories of hidden fp16 tensors survive naive conversion:

| Location | Count | Example |
|----------|-------|---------|
| `Constant` node `value` attributes | 152 | LayerNorm epsilon, attention mask constants |
| `ConstantOfShape` node `value` attributes | 1 | Padding value tensor |
| `Cast` nodes targeting FLOAT16 | varies | Residual fp16 casts |

**Symptom:** `Type Error: Type 'tensor(float16)' of input parameter (...weight_scale) of operator (DequantizeLinear)`

### Correct Pipeline

```
fp16 ONNX
  │
  ├─ 1. fix_fp16.py (convert ALL fp16 → fp32)
  │     • Initializers
  │     • Constant node attributes
  │     • ConstantOfShape attributes
  │     • Cast target types
  │     • value_info / input / output annotations
  │
  ├─ 2. quantize_dynamic (fp32 → int8)
  │
  └─ 3. fix_fp16.py AGAIN (quantizer creates fp16 scales)
        • DequantizeLinear weight_scale parameters
```

### Tools

| Script | Purpose |
|--------|---------|
| `python/convert/fix_fp16.py` | Clean ALL fp16 remnants from ONNX model |
| `python/convert/quantize.py` | Dynamic int8 quantization |
| `bench/bench_rk3588s.py` | RK3588S-specific benchmark suite |
| `python/gliner_onnx/infer_crossplatform.py` | Cross-platform inference (macOS + Linux ARM) |

---

## Test Data (inff.cc News)

Test texts sourced from [inff.cc](https://inff.cc) (PyRSS-powered multilingual news aggregator):

| Test | Language | Tokens | Content |
|------|----------|--------|---------|
| 德國民防 | zh-TW | 124 | German public opinion on Bundeswehr readiness |
| 馬德里示威 | zh-TW | 65 | Madrid anti-Sánchez protests |
| 中東衝突 | zh-TW | 92 | France-Israel + Ukraine-Russia conflicts |
| English short | en | 27 | Tim Cook / Apple |

---

## Platform Notes

### RK3588S Specifics
- **NPU (6 TOPS):** Not used. rknpu driver loaded but ORT has no RKNPUExecutionProvider. RKNPU2 SDK would require custom compilation.
- **Mali-G610 GPU:** Available (`/dev/dri/card0`) but ORT OpenCL EP not tested.
- **ARM NEON:** ORT auto-detects and uses ARM NEON SIMD for CPU inference.
- **Attention mask:** The SemplificaAI ONNX encoder only takes `input_ids` — no `attention_mask` input. This means padding tokens are fully processed, making all sequence lengths equally expensive at fixed padding.

### Optimization Opportunities
1. **Dynamic sequence length** — Remove 512-padding, pass actual token count. Short texts (27 tok) would be ~3× faster.
2. **RKNPU2** — Custom RKNN conversion could leverage the 6 TOPS NPU.
3. **Session warmup** — First inference includes graph optimization (~4s). Keep session alive for repeated calls.
4. **Batch processing** — Multiple texts per inference batch.

---

## Comparison: macOS vs CUDA vs RK3588S

| Platform | Hardware | Backend | Encoder Time | Speedup vs fp16 |
|----------|----------|---------|-------------|-----------------|
| MacBook Pro M3 | Apple Silicon | ONNX FP32 | ~13ms | — (different model) |
| Quadro T2000 | NVIDIA 4GB | PyTorch FP32 | ~94ms | — (different model) |
| **NanoPi M6** | **RK3588S** | **ONNX fp16** | **1878ms** | **1.00×** |
| **NanoPi M6** | **RK3588S** | **ONNX int8** | **853ms** | **2.20×** |

> Note: Apple/NVIDIA use `gliner-community/small-v2.5`, RK3588S uses `SemplificaAI/gliner2-multi-v1-onnx`. Different model variants, not directly comparable on speed alone.

### INT8 Precision Warning

On Apple Silicon (MPS), INT8 quantization was **destructive** (recall drops to 6.6-51.5%, see `bench/results_final.md`). The RK3588S INT8 results here are **speed-only** — NER accuracy has NOT been validated on the int8 model. This must be tested before production deployment.

RK3588S is an edge device — ~850ms for zero-shot NER on 512 tokens is acceptable for batch processing pipelines (news aggregation, log analysis) but too slow for real-time interactive use.

---

## Files Modified/Added

```
GLiNER-Forge/
├── bench/
│   └── bench_rk3588s.py          # NEW — RK3588S benchmark suite
├── python/
│   ├── convert/
│   │   └── fix_fp16.py           # NEW — fp16→fp32 cleanup tool
│   └── gliner_onnx/
│       └── infer_crossplatform.py # NEW — Linux ARM + macOS inference
└── reports/
    └── rk3588s_benchmark.md      # NEW — this report
```
