# GLiNER-Forge — Multi-Platform GLiNER Inference

Zero-shot NER (Named Entity Recognition) via GLiNER2, benchmarked across **macOS (Apple Silicon)**, **NVIDIA CUDA**, and **ARM edge (RK3588S)**.

## Two Tracks

| Track | Purpose | Runtime | Use case |
|-------|---------|---------|----------|
| `python/` | Research & iteration | MLX Python / ONNX Runtime | 快速實驗、模型轉換、精度驗證 |
| `native/` | Production FFI | MLX C++ → dylib | Swift/Dart app 嵌入 |

## Quick Start

### Python (MLX)

```bash
cd python
pip install -r requirements.txt
python gliner_mlx/infer.py
```

### Python (ONNX)

```bash
python gliner_onnx/infer.py
```

### Native build

```bash
cd native && ./build.sh
# → dist/libgliner_wrapper.dylib
```

## Model

Using `gliner2-multi-v1` (mDeBERTa-v3-base, 100+ languages).

| Format | Source | Size |
|--------|--------|------|
| MLX safetensors | `OpenMed/gliner-relex-base-v1.0-mlx` | ~900 MB |
| ONNX fp16 | `SemplificaAI/gliner2-multi-v1-onnx` | ~645 MB |
| ONNX fp32 | same | ~1.2 GB |

## Quantization Status

| Method | NER | Relation Extraction | Notes |
|--------|-----|---------------------|-------|
| FP16 | ✅ | ✅ | 推薦，精度無損 |
| INT8 | ✅ 可用 | ⚠️ 待測 | fp16→fp32→int8 三步轉換，見 `convert/fix_fp16.py` |
| INT4/Q4 | ❌ 無人測試 | ❌ | DeBERTa encoder 可能崩潰 |
| GGUF | ❌ 不可行 | ❌ | llama.cpp 不支援 encoder-only |

### INT8 on RK3588S (NanoPi M6)

| Variant | Size | Encoder Time | Speedup |
|---------|------|-------------|---------|
| fp16 | 531MB | 1878ms | 1.00× |
| **int8** | **322MB** | **853ms** | **2.20×** |

> 詳見 [`reports/rk3588s_benchmark.md`](reports/rk3588s_benchmark.md)

**⚠️ INT8 量化踩坑：** fp16 ONNX 直接做 `quantize_dynamic` 會爆，需要先清除 153+ 個隱藏的 fp16 tensor（Constant 節點屬性、ConstantOfShape、Cast target）。用 `python/convert/fix_fp16.py` 處理。

## Directory Layout

```
GLiNER-Forge/
├── python/
│   ├── gliner_mlx/      # MLX Python inference (OpenMed)
│   ├── gliner_onnx/     # ONNX Runtime inference
│   │   ├── infer.py             # macOS (CoreML)
│   │   └── infer_crossplatform.py # macOS + Linux ARM
│   ├── convert/         # to_onnx, to_mlx, quantize, fix_fp16
│   │   ├── fix_fp16.py          # fp16→fp32 cleanup (required before int8)
│   │   ├── quantize.py
│   │   ├── to_mlx.py
│   │   └── to_onnx.py
│   └── requirements.txt
├── native/
│   ├── src/             # gliner_wrapper.h/.cpp (MLX C++)
│   ├── dart/            # Dart FFI binding
│   ├── swift/           # Swift bridge
│   └── build.sh
├── bench/               # speed & accuracy benchmarks
│   ├── bench_rk3588s.py         # NanoPi M6 (RK3588S) benchmark
│   └── ...
├── reports/
│   └── rk3588s_benchmark.md     # RK3588S detailed report
├── models/              # weights (gitignored)
└── README.md
```

## CUDA Results (Quadro T2000, 4GB VRAM)

See [`bench/results_cuda.md`](bench/results_cuda.md) for full details.

| Model | VRAM | Avg ms/article | Notes |
|-------|------|----------------|-------|
| **small-v2.5** | 675 MB | **94 ms** | Best speed/VRAM ratio |
| medium-v2.5 | 836 MB | 112 ms | Marginal improvement |
| large-v2.5 | 1838 MB | 236 ms | Best precision |
| ONNX (CUDA) | — | 162 ms | Slower than PyTorch on CUDA |

**Key finding**: ONNX wins on Apple Silicon, PyTorch wins on CUDA.

## Cross-Platform Comparison

| Platform | Hardware | Backend | Best Model | Latency | VRAM/RAM |
|----------|----------|---------|------------|---------|----------|
| **Apple Silicon** | M-series (MPS) | ONNX FP32 | small-v2.5 | **13ms** | ~900MB |
| **NVIDIA CUDA** | Quadro T2000 (4GB) | PyTorch FP32 | small-v2.5 | **94ms** | 675MB |
| **ARM Edge** | RK3588S (NanoPi M6) | ONNX INT8 | gliner2-multi-v1 | **853ms** | 322MB |

### INT8 Precision Note

| Platform | INT8 Impact | Notes |
|----------|-------------|-------|
| Apple Silicon (MPS) | ❌ Destructive (recall drops to 6.6-51.5%) | ONNX quant on MPS breaks mDeBERTa |
| NVIDIA CUDA | ⚠️ Not tested | PyTorch native faster anyway |
| **ARM Edge (RK3588S)** | ✅ **Zero loss** (18/18 cases, 10 langs, 100% recall) | Full pipeline verified: encoder + span_rep + classifier |

> RK3588S INT8 accuracy validated with Wikipedia Taiwan multilingual test data (18 cases, 10 languages: zh-TW, en, ja, ko, ru, fr, es, ar, th, vi). All cases achieve 100% recall at threshold 0.3. See `bench/bench_rk3588s_accuracy.py`.

## Pipeline Recommendation by Platform

| Platform | Model | Backend | Quantization |
|----------|-------|---------|-------------|
| Apple Silicon | small-v2.5 | ONNX FP32 (th=0.1) | None |
| NVIDIA GPU | small-v2.5 | PyTorch CUDA (th=0.3) | None |
| ARM Edge (RK3588S) | gliner2-multi-v1 | ONNX INT8 | Dynamic int8 via fix_fp16.py |

## References

- [GLiNER repo](https://github.com/urchade/GLiNER)
- [GLiNER2](https://github.com/fastino-ai/GLiNER2)
- [OpenMed MLX](https://huggingface.co/OpenMed/gliner-relex-base-v1.0-mlx)
- [SemplificaAI ONNX](https://huggingface.co/SemplificaAI/gliner2-multi-v1-onnx)
- [gline-rs (Rust)](https://github.com/fbilhaut/gline-rs)
- [dart-ml-forge](~/Python/dart-ml-forge) — native wrapper pattern
