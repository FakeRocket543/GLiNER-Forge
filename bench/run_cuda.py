"""GLiNER CUDA benchmark — Quadro T2000 (4GB VRAM).

Usage:
    cd pyrss/engine && PYTHONPATH=src python3 ../../GLiNER-Forge/bench/run_cuda.py
"""
import sqlite3, time, torch, json
from pathlib import Path
from gliner import GLiNER

LABELS = ["person", "organization", "country", "city", "political party", "event"]
DB_PATH = Path(__file__).resolve().parents[2] / "pyrss" / "engine" / "data" / "pipeline.db"
MODELS = [
    "gliner-community/gliner_small-v2.5",
    "gliner-community/gliner_medium-v2.5",
    "gliner-community/gliner_large-v2.5",
]
THRESHOLDS = [0.1, 0.2, 0.3, 0.4, 0.5]


def get_samples(db_path: str, n_langs: int = 12) -> dict[str, str]:
    db = sqlite3.connect(db_path)
    samples = {}
    for row in db.execute(
        "SELECT lang, text FROM articles WHERE length(text) > 300 AND length(text) < 1500 ORDER BY RANDOM()"
    ).fetchall():
        if row[0] not in samples and len(samples) < n_langs:
            samples[row[0]] = row[1][:500]
    db.close()
    return samples


def bench_model(model_id: str, samples: dict, threshold: float = 0.3) -> dict:
    torch.cuda.empty_cache()
    t0 = time.time()
    model = GLiNER.from_pretrained(model_id)
    model.cuda()
    load_time = time.time() - t0
    vram = torch.cuda.memory_allocated() / 1e6

    # Warmup
    model.predict_entities("warmup", LABELS, threshold=threshold)

    times = []
    total_ents = 0
    for lang, text in samples.items():
        t0 = time.time()
        ents = model.predict_entities(text, LABELS, threshold=threshold)
        times.append((time.time() - t0) * 1000)
        total_ents += len(ents)

    del model
    torch.cuda.empty_cache()

    return {
        "model": model_id.split("/")[-1],
        "load_s": round(load_time, 1),
        "vram_mb": round(vram),
        "avg_ms": round(sum(times) / len(times)),
        "total_entities": total_ents,
        "per_lang_ms": {lang: round(t) for lang, t in zip(samples.keys(), times)},
    }


def main():
    # Try pipeline DB first, fallback to manual samples
    if DB_PATH.exists():
        samples = get_samples(str(DB_PATH))
    else:
        samples = {
            "en": "Mark Carney warned Alberta separatists about leaving Canada.",
            "fr": "Le président Macron a rencontré Zelensky à l'Élysée pour la guerre en Ukraine.",
            "ru": "Путин встретился с патриархом Кириллом в Кремле.",
            "ar": "أعلن وزير الخارجية الإسباني سانشيز موقفه من الحرب.",
            "es": "El presidente Milei anunció nuevas reformas económicas.",
        }

    print(f"Platform: {torch.cuda.get_device_name(0)}, VRAM: {torch.cuda.get_device_properties(0).total_mem / 1e9:.1f}GB")
    print(f"Languages: {list(samples.keys())}")
    print()

    results = []
    for model_id in MODELS:
        print(f"{'='*60}")
        print(f"  {model_id}")
        print(f"{'='*60}")
        try:
            r = bench_model(model_id, samples)
            results.append(r)
            print(f"  Load: {r['load_s']}s | VRAM: {r['vram_mb']}MB | Avg: {r['avg_ms']}ms | Entities: {r['total_entities']}")
            for lang, ms in r["per_lang_ms"].items():
                print(f"    {lang:5s}: {ms}ms")
        except Exception as e:
            print(f"  FAILED: {e}")
        print()

    # Threshold sweep on small
    print(f"\n{'='*60}")
    print("  Threshold sweep: small-v2.5")
    print(f"{'='*60}")
    model = GLiNER.from_pretrained("gliner-community/gliner_small-v2.5")
    model.cuda()
    test_text = list(samples.values())[0]
    for th in THRESHOLDS:
        ents = model.predict_entities(test_text, LABELS, threshold=th)
        print(f"  th={th}: {len(ents)} entities")
    del model
    torch.cuda.empty_cache()

    # Save results
    out_path = Path(__file__).parent / "results_cuda.json"
    json.dump(results, open(out_path, "w"), indent=2)
    print(f"\nResults saved to {out_path}")


if __name__ == "__main__":
    main()
