# GLiNER CUDA Benchmark Results

**Platform**: NVIDIA Quadro T2000 (4GB VRAM), Linux  
**Date**: 2026-05-26  
**Test**: Real news articles from pyrss pipeline, 10-12 languages  
**Labels**: person, organization, country, city, political party, event  
**Threshold**: 0.3

## Model Comparison (PyTorch CUDA FP32)

| Model | Load (s) | VRAM (MB) | Avg ms/article | Entity quality |
|-------|----------|-----------|----------------|----------------|
| **small-v2.5** | 2.5 | 675 | **94** | Good — catches most entities, some noise |
| medium-v2.5 | 81.3¹ | 836 | 112 | Good — slightly cleaner types |
| **large-v2.5** | 5.9 | 1838 | 236 | Best precision — fewer false positives |
| knowledgator/x-base | ❌ | — | — | Gated repo (needs HF token) |
| knowledgator/x-large | ❌ | — | — | Gated repo (needs HF token) |

¹ First-time download; subsequent loads ~3-6s from cache.

## ONNX vs PyTorch (small-v2.5, CUDA)

| Backend | Avg ms/article | Load (s) | Notes |
|---------|----------------|----------|-------|
| PyTorch CUDA FP32 | **94** | 2.5 | Winner on CUDA |
| ONNX CUDAExecutionProvider | 162 | 1.4 | Slower — overhead from ONNX runtime |
| ONNX CPUExecutionProvider | ~200+ | — | Not tested, worse than CUDA |

**Conclusion**: On NVIDIA CUDA, PyTorch native > ONNX. ONNX wins only on Apple Silicon / CPU-only.

## Threshold Sweep (small-v2.5, Persian news)

| Threshold | Entities found | Notes |
|-----------|---------------|-------|
| 0.1 | 10 | More recall, same precision (good) |
| 0.2 | 10 | Same as 0.1 |
| 0.3 | 7 | Balanced |
| 0.4 | 7 | Same as 0.3 |
| 0.5 | 4 | Misses some entities |

## Per-Language Quality (small-v2.5, CUDA, th=0.3)

| Lang | Entities | Sample quality |
|------|----------|---------------|
| en | 11 | ✅ Board of Peace(ORG), Gaza(city), Hamas(pol) |
| fr | 4 | ✅ Tulsi Gabbard(PER), Donald Trump(PER), Truth Social(ORG) |
| ru | 9 | ✅ Евросоюза(ORG), МОСКВА(city), РИА Новости(ORG) |
| ar | 17 | ✅ إسرائيل(city)², بن غفير(PER), لبنان(country) |
| fa | 3 | ✅ متوسلیان(PER), تهران(city) |
| es | 13 | ✅ Trump(PER), The Atlantic(ORG) |
| vi | 5 | ✅ Trung ương Đảng(ORG), Nguyễn Hải Ninh(PER) |
| nl | 6 | ✅ Tom Waes(PER), Oekraïne(country) |
| is | 8 | ✅ Vatni(PER), AP(ORG) |
| pt | 11 | ✅ Prefeitura de Zarqa(ORG) |
| it | 6 | ✅ Camila Giorgi(PER), Firenze(city) |
| zh-CN | 12 | ⚠️ Noisy — picks up French text from RFI articles |

² Type confusion: Israel tagged as "city" not "country" — threshold/label sensitivity.

## Per-Language Quality (large-v2.5, CUDA, th=0.3)

| Lang | Entities | Advantage over small |
|------|----------|---------------------|
| en | 6 | Fewer but more precise |
| fr | 5 | Clean: Tulsi Gabbard, Donald Trump, Truth Social |
| ru | 7 | Correct: Страны Евросоюза(ORG), РИА Новости(ORG) |
| ar | 11 | Better type assignment |
| fa | 5 | Cleaner: شهید متوسلیان(PER), تهران(city) |
| es | 16 | More entities (recall boost) |
| vi | 6 | ✅ Trung ương Đảng, Nguyễn Hải Ninh — same quality |
| nl | 6 | Same |
| is | 5 | Fewer but cleaner |

## VRAM Budget Analysis (T2000 4GB)

| Configuration | VRAM | Fits? |
|--------------|------|-------|
| small-v2.5 alone | 675 MB | ✅ Easy |
| large-v2.5 alone | 1838 MB | ✅ Fine |
| small + Stanza (sequential) | 675 + 660 = 1335 | ✅ if subprocess |
| large + Stanza (sequential) | 1838 + 660 = 2498 | ⚠️ Tight but OK |
| small + embedding API | 675 + 0 = 675 | ✅ Best |
| large + embedding API | 1838 + 0 = 1838 | ✅ |

## Recommendations for pyrss Pipeline

### Winner: **small-v2.5 PyTorch CUDA, threshold 0.3**

Rationale:
1. **3x faster** than large (94ms vs 236ms) → matters for 200+ articles/batch
2. **1/3 VRAM** (675MB vs 1838MB) → safe margin for T2000
3. **Comparable recall** on real news (slightly more noise but _build_glossary filters)
4. **ONNX not worth it** on CUDA — PyTorch is faster
5. Load time 2.5s (vs 6s large) helps subprocess startup

### Alternative: **large-v2.5** if precision matters more than speed
- Better for: Arabic, Persian (cleaner type assignment)
- Worse for: throughput-sensitive batches

### Configuration

```python
MODEL_ID = "gliner-community/gliner_small-v2.5"  # or large-v2.5
THRESHOLD = 0.3  # balanced recall/precision
MAX_CHARS = 500  # context window limit
```

### Not recommended
- ONNX on CUDA (slower than PyTorch)
- Quantization (INT8 destroys quality per MPS bench)
- knowledgator models (gated, need HF auth)
