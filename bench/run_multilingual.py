"""Multilingual GLiNER benchmark — measures NER recall across languages."""
import sys
from pathlib import Path
from collections import defaultdict

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "python"))
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from bench.test_data_taiwan import TEST_CASES
from gliner_mlx.infer import load_model, predict


def fuzzy_match(expected, predicted):
    """Check if expected text is substring of predicted or vice versa, and labels match."""
    return (expected["label"] == predicted.get("label") and
            (expected["text"] in predicted.get("text", "") or
             predicted.get("text", "") in expected["text"]))


def run_benchmark():
    print("Loading model...")
    pipe = load_model()
    print("Model loaded.\n")

    lang_stats = defaultdict(lambda: {"found": 0, "total": 0})

    print(f"{'Lang':<8} {'Found/Total':<14} {'Recall':<10} {'Details'}")
    print("-" * 80)

    for case in TEST_CASES:
        lang = case["lang"]
        result = predict(pipe, case["text"], case["labels"], relations=[])
        entities = result.get("entities", [])

        found = 0
        details = []
        for exp in case["expected"]:
            matched = any(fuzzy_match(exp, pred) for pred in entities)
            if matched:
                found += 1
                details.append(f"✓ {exp['text']}")
            else:
                details.append(f"✗ {exp['text']}")

        lang_stats[lang]["found"] += found
        lang_stats[lang]["total"] += len(case["expected"])

        recall = found / len(case["expected"]) if case["expected"] else 1.0
        print(f"  {lang:<6} {found}/{len(case['expected']):<12} {recall:<10.1%} {', '.join(details)}")

    # Summary
    print("\n" + "=" * 80)
    print(f"{'Language':<12} {'Found':<8} {'Total':<8} {'Recall'}")
    print("-" * 40)

    overall_found = overall_total = 0
    for lang, stats in sorted(lang_stats.items()):
        recall = stats["found"] / stats["total"] if stats["total"] else 1.0
        print(f"  {lang:<10} {stats['found']:<8} {stats['total']:<8} {recall:.1%}")
        overall_found += stats["found"]
        overall_total += stats["total"]

    overall_recall = overall_found / overall_total if overall_total else 1.0
    print("-" * 40)
    print(f"  {'OVERALL':<10} {overall_found:<8} {overall_total:<8} {overall_recall:.1%}")


if __name__ == "__main__":
    run_benchmark()
