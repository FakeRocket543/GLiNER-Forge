"""Benchmark: verify NER accuracy across backends (golden test)."""
import json
from pathlib import Path

# Golden test cases — expected entities
GOLDEN = [
    {
        "text": "Tim Cook is the CEO of Apple Inc., headquartered in Cupertino, California.",
        "labels": ["person", "organization", "location"],
        "expected": [
            {"text": "Tim Cook", "label": "person"},
            {"text": "Apple Inc.", "label": "organization"},
            {"text": "Cupertino, California", "label": "location"},
        ],
    },
    {
        "text": "Bill Gates founded Microsoft in Albuquerque.",
        "labels": ["person", "organization", "location"],
        "expected": [
            {"text": "Bill Gates", "label": "person"},
            {"text": "Microsoft", "label": "organization"},
            {"text": "Albuquerque", "label": "location"},
        ],
    },
]


def check_entities(predicted: list[dict], expected: list[dict]) -> dict:
    """Check if expected entities are found in predictions."""
    found = 0
    for exp in expected:
        for pred in predicted:
            if exp["label"] == pred.get("label") and exp["text"].lower() in pred.get("text", "").lower():
                found += 1
                break
    return {"recall": found / len(expected) if expected else 1.0, "found": found, "total": len(expected)}


def test_gliner_pytorch():
    from gliner import GLiNER
    model = GLiNER.from_pretrained("urchade/gliner_medium-v2.1")
    results = []
    for case in GOLDEN:
        entities = model.predict_entities(case["text"], case["labels"])
        r = check_entities(entities, case["expected"])
        results.append(r)
    return results


def test_openmed_mlx():
    import sys
    sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "python"))
    from gliner_mlx.infer import load_model, predict
    pipe = load_model()
    results = []
    for case in GOLDEN:
        out = predict(pipe, case["text"], case["labels"], relations=[])
        r = check_entities(out.get("entities", []), case["expected"])
        results.append(r)
    return results


if __name__ == "__main__":
    print("=== GLiNER Accuracy (Golden Test) ===\n")

    for name, fn in [("PyTorch", test_gliner_pytorch), ("MLX", test_openmed_mlx)]:
        try:
            results = fn()
            avg_recall = sum(r["recall"] for r in results) / len(results)
            print(f"  {name:10s}: recall={avg_recall:.1%} ({results})")
        except Exception as e:
            print(f"  {name:10s}: SKIP ({e})")
