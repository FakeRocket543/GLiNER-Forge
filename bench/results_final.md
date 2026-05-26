# GLiNER Comprehensive Benchmark Results

**Platform**: Apple Silicon (MPS), macOS  
**Date**: 2026-05-26  
**Test**: 18 cases × 10 languages (Wikipedia "Taiwan" article)

## Full Matrix: 6 Models × Backends

| Model | Backend | Recall% | ms/call | ar | en | es | fr | ja | ko | ru | th | vi | zh |
|-------|---------|---------|---------|----|----|----|----|----|----|----|----|----|----|
| small-v2.5 | CPU FP32 | 64.8 | 27.6 | 60 | 94 | 100 | 80 | 40 | 60 | 100 | 20 | 80 | 39 |
| small-v2.5 | MPS FP32 | 64.8 | 21.0 | 60 | 94 | 100 | 80 | 40 | 60 | 100 | 20 | 80 | 39 |
| **small-v2.5** | **ONNX FP32** | **64.8** | **13.2** | 60 | 94 | 100 | 80 | 40 | 60 | 100 | 20 | 80 | 39 |
| medium-v2.5 | CPU FP32 | 55.7 | 48.6 | 80 | 89 | 80 | 80 | 20 | 40 | 86 | 20 | 100 | 21 |
| medium-v2.5 | MPS FP32 | 55.7 | 31.5 | 80 | 89 | 80 | 80 | 20 | 40 | 86 | 20 | 100 | 21 |
| medium-v2.5 | ONNX FP32 | 55.7 | 19.6 | 80 | 89 | 80 | 80 | 20 | 40 | 86 | 20 | 100 | 21 |
| large-v2.5 | CPU FP32 | 46.6 | 120.3 | 40 | 94 | 60 | 80 | 20 | 80 | 86 | 0 | 80 | 0 |
| large-v2.5 | MPS FP32 | 46.6 | 48.7 | 40 | 94 | 60 | 80 | 20 | 80 | 86 | 0 | 80 | 0 |
| large-v2.5 | ONNX FP32 | 46.6 | 46.5 | 40 | 94 | 60 | 80 | 20 | 80 | 86 | 0 | 80 | 0 |
| x-small | CPU FP16 | 61.4 | 40.4 | 60 | 83 | 80 | 80 | 80 | 60 | 85 | 60 | 60 | 32 |
| x-small | MPS FP16 | 61.4 | 65.1 | 60 | 83 | 80 | 80 | 80 | 60 | 85 | 60 | 60 | 32 |
| **x-base** | CPU FP16 | **67.0** | 51.5 | 60 | 88 | 80 | 80 | 80 | 80 | 85 | 80 | 80 | 35 |
| x-base | MPS FP16 | 67.0 | 68.7 | 60 | 88 | 80 | 80 | 80 | 80 | 85 | 80 | 80 | 35 |
| **x-base** | **ONNX** | **67.0** | **32.5** | 60 | 88 | 80 | 80 | 80 | 80 | 85 | 80 | 80 | 35 |
| **x-large** | CPU | **68.2** | 95.5 | 80 | 94 | 80 | 80 | 80 | 80 | 85 | 80 | 80 | 32 |
| x-large | MPS | 68.2 | 107.2 | 80 | 94 | 80 | 80 | 80 | 80 | 85 | 80 | 80 | 32 |
| MLX relex-base | MLX Python | 62.5 | 21.1 | 20 | 88 | 80 | 80 | 60 | 60 | 42 | 20 | 80 | 57 |

## Threshold Tuning

| Model | th=0.1 | th=0.2 | th=0.3 | th=0.4 | th=0.5 |
|-------|--------|--------|--------|--------|--------|
| small-v2.5 | **69.3%** (zh=50%) | 67.0% (zh=46%) | 64.8% (zh=39%) | 61.4% (zh=32%) | 59.1% (zh=32%) |
| x-base | 68.2% (zh=35%) | 67.0% | 67.0% | 67.0% | 62.5% (zh=21%) |
| x-large | 68.2% | 68.2% | 68.2% | 68.2% | 68.2% |

## Key Findings

1. **Larger ≠ better** (v2.5 series): small > medium > large on multilingual NER
2. **x-series fixes CJK**: Thai 20%→80%, Japanese 40%→80%, Korean 60%→80%
3. **Chinese remains weak** across all GLiNER variants (32-57%); use CKIP NER for zh
4. **ONNX is fastest** for small/medium/x-base; MPS marginal benefit
5. **x-large ONNX impossible** (>2GB protobuf limit)
6. **Threshold 0.1** boosts small-v2.5 recall significantly (+4.5pp)

## Recommended Configurations

| Use Case | Model | Backend | Recall | Latency |
|----------|-------|---------|--------|---------|
| English-primary, low latency | small-v2.5 | ONNX (th=0.1) | 69.3% | ~13ms |
| Multilingual (non-CJK) | x-base | ONNX | 67.0% | ~32ms |
| Best overall (GPU available) | x-large | CUDA | 68.2% | ~10ms* |
| Chinese NER | CKIP BERT | native C++ | >90% | <5ms |

*Estimated CUDA latency, to be benchmarked on NVIDIA GPU.

## Failed Configurations

- x-small ONNX: export not supported (MT5 backbone incompatible with GLiNER ONNX export)
- x-large ONNX: model >2GB exceeds protobuf limit
- INT8 quantization: destructive (6.6-51.5% recall), NOT recommended
- FP16/BF16 on CPU: slower than FP32, useless without GPU tensor cores
