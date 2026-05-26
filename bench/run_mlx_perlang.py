import sys, time
sys.path.insert(0, '/Users/fl/projets/GLiNER')
sys.path.insert(0, '/Users/fl/projets/GLiNER/bench')
from test_data_taiwan import TEST_CASES
from huggingface_hub import snapshot_download
from openmed.mlx.inference import GLiNERRelexMLXPipeline

model_path = snapshot_download('OpenMed/gliner-relex-base-v1.0-mlx')
pipe = GLiNERRelexMLXPipeline(model_path)

# Warmup
for tc in TEST_CASES[:3]:
    pipe.inference(tc['text'], labels=tc['labels'], relations=[], threshold=0.3)

# Timed run
from collections import defaultdict
lang_results = defaultdict(lambda: {'found': 0, 'total': 0})
times = []

for _ in range(3):
    for tc in TEST_CASES:
        t0 = time.perf_counter()
        result = pipe.inference(tc['text'], labels=tc['labels'], relations=[], threshold=0.3)
        times.append(time.perf_counter() - t0)
        
        predicted = result.get('entities', [])
        for exp in tc['expected']:
            found = any(
                (exp['text'].lower() in p['text'].lower() or p['text'].lower() in exp['text'].lower())
                and exp['label'] == p['label']
                for p in predicted
            )
            if _ == 0:  # count only first iteration
                lang_results[tc['lang']]['total'] += 1
                if found:
                    lang_results[tc['lang']]['found'] += 1

avg_ms = sum(times) / len(times) * 1000
total_found = sum(v['found'] for v in lang_results.values())
total_total = sum(v['total'] for v in lang_results.values())
recall = total_found / total_total * 100

print(f'\nMLX (OpenMed gliner-relex-base) Results:')
print(f'  Overall: {total_found}/{total_total} = {recall:.1f}% recall')
print(f'  Avg: {avg_ms:.1f} ms/call')
print(f'\n  Per-language:')
for lang in sorted(lang_results.keys()):
    r = lang_results[lang]
    pct = r['found']/r['total']*100 if r['total'] else 0
    print(f'    {lang:8s} {r["found"]}/{r["total"]} = {pct:.0f}%')
