"""
Full matrix benchmark: all models × all quantizations × all backends × all languages.
Based on Wikipedia: Taiwan test data.

Output: bench/reports/full_matrix_report.md
"""
import sys
import os
import time
import json
import traceback
from pathlib import Path
from dataclasses import dataclass, field

sys.path.insert(0, str(Path(__file__).parent))
sys.path.insert(0, str(Path(__file__).parent.parent / "src"))

from test_data_taiwan import TEST_CASES

# ─── Config ───

MODELS_DIR = Path(__file__).parent.parent / "models"
REPORT_DIR = Path(__file__).parent / "reports"
REPORT_DIR.mkdir(exist_ok=True)

THRESHOLD = 0.3
WARMUP = 1
TIMED = 3


@dataclass
class TestResult:
    model: str
    variant: str
    backend: str
    lang: str
    text_preview: str
    entities_found: list = field(default_factory=list)
    expected: list = field(default_factory=list)
    precision: float = 0.0
    recall: float = 0.0
    f1: float = 0.0
    latency_ms: float = 0.0
    error: str = ""


def calc_metrics(found: list, expected: list) -> tuple:
    """Calculate precision, recall, F1 based on text+label match."""
    found_set = {(e.get("text", "").strip(), e.get("label", "")) for e in found}
    expected_set = {(e["text"], e["label"]) for e in expected}
    if not found_set and not expected_set:
        return 1.0, 1.0, 1.0
    tp = len(found_set & expected_set)
    p = tp / len(found_set) if found_set else 0.0
    r = tp / len(expected_set) if expected_set else 0.0
    f1 = 2 * p * r / (p + r) if (p + r) > 0 else 0.0
    return p, r, f1


# ─── Backend: ONNX (our standalone pipeline) ───

def test_onnx_standalone(model_dir: str, variant: str, provider: str, test_cases: list) -> list:
    """Test using our GLiNERStandalone ONNX pipeline."""
    from gliner_forge.onnx_infer import GLiNERStandalone

    # Determine onnx path
    model_path = Path(model_dir)
    if variant == "fp32":
        onnx_file = model_path / "model.onnx"
    elif variant == "fp16":
        onnx_file = model_path / "model_fp16.onnx"
    elif variant == "int8":
        onnx_file = model_path / "model_quantized.onnx"
    else:
        onnx_file = model_path / "model.onnx"

    if not onnx_file.exists():
        return [TestResult(model=model_path.name, variant=variant, backend=f"onnx-{provider}",
                           lang="all", text_preview="", error=f"File not found: {onnx_file}")]

    # Temporarily copy/symlink the onnx file as model.onnx for our pipeline
    actual_model_onnx = model_path / "model.onnx"
    need_restore = False
    backup = None
    if onnx_file != actual_model_onnx:
        if actual_model_onnx.exists():
            backup = actual_model_onnx.with_suffix(".onnx.bak")
            os.rename(actual_model_onnx, backup)
            need_restore = True
        os.symlink(onnx_file, actual_model_onnx)

    try:
        providers = [provider, "CPUExecutionProvider"] if provider != "CPUExecutionProvider" else ["CPUExecutionProvider"]
        model = GLiNERStandalone(str(model_path), providers=providers)

        results = []
        for tc in test_cases:
            # Warmup
            for _ in range(WARMUP):
                model.predict_entities(tc["text"], tc["labels"], threshold=THRESHOLD)

            # Timed
            t0 = time.perf_counter()
            for _ in range(TIMED):
                entities = model.predict_entities(tc["text"], tc["labels"], threshold=THRESHOLD)
            elapsed = (time.perf_counter() - t0) / TIMED * 1000

            p, r, f1 = calc_metrics(entities, tc.get("expected", []))
            results.append(TestResult(
                model=model_path.name, variant=variant, backend=f"onnx-{provider.replace('ExecutionProvider','')}",
                lang=tc["lang"], text_preview=tc["text"][:40],
                entities_found=entities, expected=tc.get("expected", []),
                precision=p, recall=r, f1=f1, latency_ms=elapsed,
            ))
        return results
    except Exception as e:
        return [TestResult(model=model_path.name, variant=variant, backend=f"onnx-{provider}",
                           lang="all", text_preview="", error=f"{type(e).__name__}: {e}")]
    finally:
        if need_restore:
            os.unlink(actual_model_onnx)
            if backup:
                os.rename(backup, actual_model_onnx)


# ─── Backend: PyTorch (gliner library) ───

def test_pytorch(model_name: str, device: str, test_cases: list) -> list:
    """Test using gliner library with PyTorch."""
    from gliner import GLiNER

    try:
        model = GLiNER.from_pretrained(model_name)
        if device == "mps":
            import torch
            if torch.backends.mps.is_available():
                model = model.to("mps")
            else:
                return [TestResult(model=model_name.split("/")[-1], variant="pytorch", backend=f"pytorch-{device}",
                                   lang="all", text_preview="", error="MPS not available")]
    except Exception as e:
        return [TestResult(model=model_name.split("/")[-1], variant="pytorch", backend=f"pytorch-{device}",
                           lang="all", text_preview="", error=f"{type(e).__name__}: {e}")]

    results = []
    for tc in test_cases:
        try:
            for _ in range(WARMUP):
                model.predict_entities(tc["text"], tc["labels"], threshold=THRESHOLD)

            t0 = time.perf_counter()
            for _ in range(TIMED):
                entities = model.predict_entities(tc["text"], tc["labels"], threshold=THRESHOLD)
            elapsed = (time.perf_counter() - t0) / TIMED * 1000

            # Normalize format
            norm_entities = [{"text": e["text"], "label": e["label"], "score": e["score"]} for e in entities]
            p, r, f1 = calc_metrics(norm_entities, tc.get("expected", []))
            results.append(TestResult(
                model=model_name.split("/")[-1], variant="pytorch", backend=f"pytorch-{device}",
                lang=tc["lang"], text_preview=tc["text"][:40],
                entities_found=norm_entities, expected=tc.get("expected", []),
                precision=p, recall=r, f1=f1, latency_ms=elapsed,
            ))
        except Exception as e:
            results.append(TestResult(
                model=model_name.split("/")[-1], variant="pytorch", backend=f"pytorch-{device}",
                lang=tc["lang"], text_preview=tc["text"][:40], error=str(e),
            ))
    return results


# ─── Backend: GLiNER-X (PyTorch) ───

def test_glinerx(model_name: str, device: str, test_cases: list) -> list:
    """Test GLiNER-X models."""
    return test_pytorch(model_name, device, test_cases)


# ─── Backend: GLiNER2 (multi-component ONNX) ───

def test_gliner2(model_name: str, test_cases: list) -> list:
    """Test GLiNER2 multi-component ONNX pipeline."""
    try:
        from gliner2 import GLiNER2
        model = GLiNER2.from_pretrained(model_name)
    except Exception as e:
        return [TestResult(model=model_name.split("/")[-1], variant="onnx-multi", backend="gliner2",
                           lang="all", text_preview="", error=f"{type(e).__name__}: {e}")]

    results = []
    for tc in test_cases:
        try:
            for _ in range(WARMUP):
                model.extract_entities(tc["text"], tc["labels"], threshold=THRESHOLD,
                                       include_confidence=True, include_spans=True)

            t0 = time.perf_counter()
            for _ in range(TIMED):
                raw = model.extract_entities(tc["text"], tc["labels"], threshold=THRESHOLD,
                                             include_confidence=True, include_spans=True)
            elapsed = (time.perf_counter() - t0) / TIMED * 1000

            # Normalize GLiNER2 output format
            entities = []
            if isinstance(raw, dict):
                for label, items in raw.items():
                    if isinstance(items, list):
                        for item in items:
                            if isinstance(item, dict):
                                entities.append({"text": item.get("text", item.get("span", "")),
                                                 "label": label,
                                                 "score": item.get("confidence", 0)})
                            elif isinstance(item, str):
                                entities.append({"text": item, "label": label, "score": 0})

            p, r, f1 = calc_metrics(entities, tc.get("expected", []))
            results.append(TestResult(
                model="gliner2-multi-v1", variant="onnx-multi", backend="gliner2",
                lang=tc["lang"], text_preview=tc["text"][:40],
                entities_found=entities, expected=tc.get("expected", []),
                precision=p, recall=r, f1=f1, latency_ms=elapsed,
            ))
        except Exception as e:
            results.append(TestResult(
                model="gliner2-multi-v1", variant="onnx-multi", backend="gliner2",
                lang=tc["lang"], text_preview=tc["text"][:40], error=str(e),
            ))
    return results


# ─── Backend: MLX (OpenMed) ───

def test_mlx(test_cases: list) -> list:
    """Test MLX pipeline (different model - relation extraction)."""
    try:
        from openmed.mlx.inference import GLiNERRelexMLXPipeline
        from huggingface_hub import snapshot_download
        model_path = snapshot_download("OpenMed/gliner-relex-base-v1.0-mlx")
        pipeline = GLiNERRelexMLXPipeline(model_path)
    except Exception as e:
        return [TestResult(model="openmed-relex-base-mlx", variant="mlx", backend="mlx",
                           lang="all", text_preview="", error=f"{type(e).__name__}: {e}")]

    results = []
    for tc in test_cases:
        try:
            for _ in range(WARMUP):
                pipeline.inference(tc["text"], labels=tc["labels"], relations=[], threshold=THRESHOLD)

            t0 = time.perf_counter()
            for _ in range(TIMED):
                raw = pipeline.inference(tc["text"], labels=tc["labels"], relations=[], threshold=THRESHOLD)
            elapsed = (time.perf_counter() - t0) / TIMED * 1000

            entities = [{"text": e["text"], "label": e["label"], "score": e.get("score", 0)}
                        for e in raw.get("entities", [])]

            p, r, f1 = calc_metrics(entities, tc.get("expected", []))
            results.append(TestResult(
                model="openmed-relex-base-mlx", variant="mlx", backend="mlx",
                lang=tc["lang"], text_preview=tc["text"][:40],
                entities_found=entities, expected=tc.get("expected", []),
                precision=p, recall=r, f1=f1, latency_ms=elapsed,
            ))
        except Exception as e:
            results.append(TestResult(
                model="openmed-relex-base-mlx", variant="mlx", backend="mlx",
                lang=tc["lang"], text_preview=tc["text"][:40], error=str(e),
            ))
    return results


# ─── Backend: C++ native ───

def test_cpp_native(model_dir: str, test_cases: list) -> list:
    """Test C++ native wrapper via subprocess."""
    import subprocess
    binary = Path(__file__).parent.parent / "native" / "test_gliner"
    if not binary.exists():
        return [TestResult(model=Path(model_dir).name, variant="fp32", backend="cpp-native",
                           lang="all", text_preview="", error="test_gliner binary not found")]

    results = []
    for tc in test_cases:
        try:
            labels_str = ",".join(tc["labels"])
            # We need a proper CLI interface; for now use the Python ctypes approach
            # Skip if binary doesn't support CLI args for text/labels
            results.append(TestResult(
                model=Path(model_dir).name, variant="fp32", backend="cpp-native",
                lang=tc["lang"], text_preview=tc["text"][:40],
                error="CLI interface not yet implemented for batch testing",
            ))
        except Exception as e:
            results.append(TestResult(
                model=Path(model_dir).name, variant="fp32", backend="cpp-native",
                lang=tc["lang"], text_preview=tc["text"][:40], error=str(e),
            ))
    return results


# ─── Report Generation ───

def generate_report(all_results: list) -> str:
    """Generate markdown report."""
    lines = []
    lines.append("# GLiNER Full Matrix Benchmark Report")
    lines.append(f"\n**Date:** {time.strftime('%Y-%m-%d %H:%M')}")
    lines.append(f"**Platform:** macOS Apple Silicon")
    lines.append(f"**Test cases:** {len(TEST_CASES)} (10 languages, Wikipedia: Taiwan)")
    lines.append(f"**Threshold:** {THRESHOLD}")
    lines.append(f"**Timing:** {TIMED} runs after {WARMUP} warmup")

    # Summary table
    lines.append("\n---\n## Summary by Model × Backend\n")
    lines.append("| Model | Variant | Backend | Avg F1 | Avg Latency | Languages OK | Errors |")
    lines.append("|-------|---------|---------|--------|-------------|--------------|--------|")

    # Group results
    from collections import defaultdict
    groups = defaultdict(list)
    for r in all_results:
        key = (r.model, r.variant, r.backend)
        groups[key].append(r)

    for (model, variant, backend), results in sorted(groups.items()):
        errors = [r for r in results if r.error]
        ok = [r for r in results if not r.error]
        avg_f1 = sum(r.f1 for r in ok) / len(ok) if ok else 0
        avg_lat = sum(r.latency_ms for r in ok) / len(ok) if ok else 0
        langs_ok = len(set(r.lang for r in ok))
        lines.append(f"| {model} | {variant} | {backend} | {avg_f1:.3f} | {avg_lat:.0f}ms | {langs_ok}/10 | {len(errors)} |")

    # Per-language breakdown
    lines.append("\n---\n## Per-Language F1 Scores\n")

    # Get all unique model+backend combos
    combos = sorted(set((r.model, r.variant, r.backend) for r in all_results if not r.error))
    langs = ["zh-TW", "en", "ja", "ko", "ru", "fr", "es", "ar", "th", "vi"]

    header = "| Model | Variant | Backend | " + " | ".join(langs) + " |"
    sep = "|-------|---------|---------|" + "|".join(["------"] * len(langs)) + "|"
    lines.append(header)
    lines.append(sep)

    for (model, variant, backend) in combos:
        row = f"| {model} | {variant} | {backend} |"
        for lang in langs:
            lang_results = [r for r in all_results
                           if r.model == model and r.variant == variant
                           and r.backend == backend and r.lang == lang and not r.error]
            if lang_results:
                avg_f1 = sum(r.f1 for r in lang_results) / len(lang_results)
                row += f" {avg_f1:.2f} |"
            else:
                row += " — |"
        lines.append(row)

    # Detailed per-test-case results
    lines.append("\n---\n## Detailed Results\n")

    for (model, variant, backend), results in sorted(groups.items()):
        lines.append(f"\n### {model} / {variant} / {backend}\n")
        if any(r.error for r in results if r.lang == "all"):
            for r in results:
                if r.error and r.lang == "all":
                    lines.append(f"**ERROR:** {r.error}\n")
            continue

        lines.append("| Lang | Text | F1 | P | R | Latency | Found | Expected |")
        lines.append("|------|------|----|----|---|---------|-------|----------|")
        for r in results:
            if r.error:
                lines.append(f"| {r.lang} | {r.text_preview} | ERROR | — | — | — | — | {r.error} |")
            else:
                found_str = ", ".join(f"{e['text']}" for e in r.entities_found[:5])
                if len(r.entities_found) > 5:
                    found_str += f" +{len(r.entities_found)-5}"
                exp_str = ", ".join(f"{e['text']}" for e in r.expected[:5])
                lines.append(f"| {r.lang} | {r.text_preview}… | {r.f1:.2f} | {r.precision:.2f} | {r.recall:.2f} | {r.latency_ms:.0f}ms | {found_str} | {exp_str} |")

    # Quantization comparison
    lines.append("\n---\n## Quantization Impact\n")
    lines.append("| Model | fp32 F1 | fp16 F1 | int8 F1 | fp16 Δ | int8 Δ |")
    lines.append("|-------|---------|---------|---------|--------|--------|")

    for model_name in ["small-v2.5", "medium-v2.5", "large-v2.5"]:
        f1s = {}
        for variant in ["fp32", "fp16", "int8"]:
            vresults = [r for r in all_results
                       if r.model == model_name and r.variant == variant
                       and "onnx" in r.backend and not r.error]
            if vresults:
                f1s[variant] = sum(r.f1 for r in vresults) / len(vresults)

        if "fp32" in f1s:
            fp32 = f1s.get("fp32", 0)
            fp16_str = f"{f1s['fp16']:.3f}" if "fp16" in f1s else "—"
            int8_str = f"{f1s['int8']:.3f}" if "int8" in f1s else "—"
            fp16_d = f"{f1s['fp16']-fp32:+.3f}" if "fp16" in f1s else "—"
            int8_d = f"{f1s['int8']-fp32:+.3f}" if "int8" in f1s else "—"
            lines.append(f"| {model_name} | {fp32:.3f} | {fp16_str} | {int8_str} | {fp16_d} | {int8_d} |")

    return "\n".join(lines)


# ─── Main ───

def main():
    all_results = []
    total_start = time.time()

    print("=" * 70)
    print("GLiNER Full Matrix Benchmark")
    print("=" * 70)

    # ─── Phase 1: ONNX Standalone (our pipeline) ───
    onnx_tests = [
        # (model_dir, variant, display_name)
        (str(MODELS_DIR / "onnx" / "small-v2.5"), "fp32", "small-v2.5"),
        (str(MODELS_DIR / "onnx" / "small-v2.5"), "fp16", "small-v2.5"),
        (str(MODELS_DIR / "onnx" / "small-v2.5"), "int8", "small-v2.5"),
        (str(MODELS_DIR / "onnx" / "medium-v2.5"), "fp32", "medium-v2.5"),
        (str(MODELS_DIR / "onnx" / "medium-v2.5"), "fp16", "medium-v2.5"),
        (str(MODELS_DIR / "onnx" / "medium-v2.5"), "int8", "medium-v2.5"),
        (str(MODELS_DIR / "large-v2.5"), "fp32", "large-v2.5"),
    ]

    for model_dir, variant, name in onnx_tests:
        for provider in ["CPUExecutionProvider", "CoreMLExecutionProvider"]:
            prov_short = provider.replace("ExecutionProvider", "")
            print(f"\n[ONNX] {name} / {variant} / {prov_short}...")
            try:
                results = test_onnx_standalone(model_dir, variant, provider, TEST_CASES)
                all_results.extend(results)
                ok = [r for r in results if not r.error]
                if ok:
                    avg_f1 = sum(r.f1 for r in ok) / len(ok)
                    avg_ms = sum(r.latency_ms for r in ok) / len(ok)
                    print(f"  → F1={avg_f1:.3f} latency={avg_ms:.0f}ms ({len(ok)} cases OK)")
                else:
                    print(f"  → ERROR: {results[0].error if results else 'no results'}")
            except Exception as e:
                print(f"  → EXCEPTION: {e}")
                all_results.append(TestResult(model=name, variant=variant, backend=f"onnx-{prov_short}",
                                             lang="all", text_preview="", error=str(e)))

    # ─── Phase 2: PyTorch + MPS ───
    pytorch_models = [
        "gliner-community/gliner_small-v2.5",
        "gliner-community/gliner_medium-v2.5",
        "gliner-community/gliner_large-v2.5",
    ]

    for model_name in pytorch_models:
        for device in ["cpu", "mps"]:
            print(f"\n[PyTorch] {model_name.split('/')[-1]} / {device}...")
            try:
                results = test_pytorch(model_name, device, TEST_CASES)
                all_results.extend(results)
                ok = [r for r in results if not r.error]
                if ok:
                    avg_f1 = sum(r.f1 for r in ok) / len(ok)
                    avg_ms = sum(r.latency_ms for r in ok) / len(ok)
                    print(f"  → F1={avg_f1:.3f} latency={avg_ms:.0f}ms ({len(ok)} cases OK)")
                else:
                    print(f"  → ERROR: {results[0].error if results else 'no results'}")
            except Exception as e:
                print(f"  → EXCEPTION: {e}")
                traceback.print_exc()

    # ─── Phase 3: GLiNER-X ───
    glinerx_models = [
        "knowledgator/gliner-x-small",
        "knowledgator/gliner-x-base",
        "knowledgator/gliner-x-large",
    ]

    for model_name in glinerx_models:
        for device in ["cpu", "mps"]:
            print(f"\n[GLiNER-X] {model_name.split('/')[-1]} / {device}...")
            try:
                results = test_glinerx(model_name, device, TEST_CASES)
                all_results.extend(results)
                ok = [r for r in results if not r.error]
                if ok:
                    avg_f1 = sum(r.f1 for r in ok) / len(ok)
                    avg_ms = sum(r.latency_ms for r in ok) / len(ok)
                    print(f"  → F1={avg_f1:.3f} latency={avg_ms:.0f}ms ({len(ok)} cases OK)")
                else:
                    print(f"  → ERROR: {results[0].error if results else 'no results'}")
            except Exception as e:
                print(f"  → EXCEPTION: {e}")

    # ─── Phase 4: GLiNER2 ───
    print(f"\n[GLiNER2] multi-v1...")
    try:
        results = test_gliner2("SemplificaAI/gliner2-multi-v1", TEST_CASES)
        all_results.extend(results)
        ok = [r for r in results if not r.error]
        if ok:
            avg_f1 = sum(r.f1 for r in ok) / len(ok)
            print(f"  → F1={avg_f1:.3f} ({len(ok)} cases OK)")
        else:
            print(f"  → ERROR: {results[0].error if results else 'no results'}")
    except Exception as e:
        print(f"  → EXCEPTION: {e}")

    # ─── Phase 5: MLX ───
    print(f"\n[MLX] OpenMed relex-base...")
    try:
        results = test_mlx(TEST_CASES)
        all_results.extend(results)
        ok = [r for r in results if not r.error]
        if ok:
            avg_f1 = sum(r.f1 for r in ok) / len(ok)
            print(f"  → F1={avg_f1:.3f} ({len(ok)} cases OK)")
        else:
            print(f"  → ERROR: {results[0].error if results else 'no results'}")
    except Exception as e:
        print(f"  → EXCEPTION: {e}")

    # ─── Phase 6: C++ native ───
    print(f"\n[C++] native small-v2.5...")
    results = test_cpp_native(str(MODELS_DIR / "small-v2.5"), TEST_CASES)
    all_results.extend(results)

    # ─── Generate Report ───
    elapsed_total = time.time() - total_start
    print(f"\n{'='*70}")
    print(f"Total time: {elapsed_total:.0f}s")
    print(f"Total test points: {len(all_results)}")
    print(f"Generating report...")

    report = generate_report(all_results)
    report += f"\n\n---\n*Total benchmark time: {elapsed_total:.0f}s*\n"

    report_path = REPORT_DIR / "full_matrix_report.md"
    report_path.write_text(report)
    print(f"Report saved: {report_path}")

    # Also save raw JSON
    json_path = REPORT_DIR / "full_matrix_raw.json"
    json_data = []
    for r in all_results:
        json_data.append({
            "model": r.model, "variant": r.variant, "backend": r.backend,
            "lang": r.lang, "text_preview": r.text_preview,
            "precision": r.precision, "recall": r.recall, "f1": r.f1,
            "latency_ms": r.latency_ms, "error": r.error,
            "entities_found": r.entities_found,
            "expected": r.expected,
        })
    json_path.write_text(json.dumps(json_data, ensure_ascii=False, indent=2))
    print(f"Raw data saved: {json_path}")


if __name__ == "__main__":
    main()
