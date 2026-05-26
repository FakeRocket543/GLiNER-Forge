# GLiNER — Local Inference on Apple Silicon

Zero-shot NER (Named Entity Recognition) via GLiNER2, optimized for macOS.

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
| INT8 | ⚠️ 可用 | ❌ 壞掉 | 僅 NER 場景 |
| INT4/Q4 | ❌ 無人測試 | ❌ | DeBERTa encoder 可能崩潰 |
| GGUF | ❌ 不可行 | ❌ | llama.cpp 不支援 encoder-only |

## Directory Layout

```
GLiNER/
├── python/
│   ├── gliner_mlx/      # MLX Python inference (OpenMed)
│   ├── gliner_onnx/     # ONNX Runtime inference
│   ├── convert/         # to_onnx, to_mlx, quantize
│   └── requirements.txt
├── native/
│   ├── src/             # gliner_wrapper.h/.cpp (MLX C++)
│   ├── dart/            # Dart FFI binding
│   ├── swift/           # Swift bridge
│   └── build.sh
├── models/              # weights (gitignored)
├── bench/               # speed & accuracy benchmarks
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

## References

- [GLiNER repo](https://github.com/urchade/GLiNER)
- [GLiNER2](https://github.com/fastino-ai/GLiNER2)
- [OpenMed MLX](https://huggingface.co/OpenMed/gliner-relex-base-v1.0-mlx)
- [SemplificaAI ONNX](https://huggingface.co/SemplificaAI/gliner2-multi-v1-onnx)
- [gline-rs (Rust)](https://github.com/fbilhaut/gline-rs)
- [dart-ml-forge](~/Python/dart-ml-forge) — native wrapper pattern
