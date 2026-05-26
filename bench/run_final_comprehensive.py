"""Final comprehensive GLiNER benchmark: 6 models × backends × thresholds."""
import sys, time, gc, os
sys.path.insert(0, '/Users/fl/projets/GLiNER')
sys.path.insert(0, '/Users/fl/projets/GLiNER/bench')
os.environ["TOKENIZERS_PARALLELISM"] = "false"

import torch
from collections import defaultdict
from test_data_taiwan import TEST_CASES
from gliner import GLiNER

LANGS = ['ar','en','es','fr','ja','ko','ru','th','vi','zh-TW']

def evaluate(model, threshold=0.3):
    lang_results = defaultdict(lambda: {'found': 0, 'total': 0})
    times = []
    for tc in TEST_CASES:
        t0 = time.perf_counter()
        try:
            preds = model.predict_entities(tc['text'], tc['labels'], threshold=threshold)
        except:
            preds = []
        times.append(time.perf_counter() - t0)
        for exp in tc['expected']:
            found = any(
                (exp['text'].lower() in p['text'].lower() or p['text'].lower() in exp['text'].lower())
                and exp['label'] == p['label']
                for p in preds
            )
            lang_results[tc['lang']]['total'] += 1
            if found:
                lang_results[tc['lang']]['found'] += 1
    total_f = sum(v['found'] for v in lang_results.values())
    total_t = sum(v['total'] for v in lang_results.values())
    return total_f / total_t * 100, sum(times)/len(times)*1000, lang_results

def lang_cols(lang):
    cols = ''
    for l in LANGS:
        if l in lang and lang[l]['total'] > 0:
            cols += f"{lang[l]['found']*100//lang[l]['total']:<5}"
        else:
            cols += f"{'--':<5}"
    return cols

def cleanup():
    gc.collect()
    if torch.backends.mps.is_available():
        torch.mps.empty_cache()

MODELS = [
    ('small-v2.5',  'gliner-community/gliner_small-v2.5'),
    ('medium-v2.5', 'gliner-community/gliner_medium-v2.5'),
    ('large-v2.5',  'gliner-community/gliner_large-v2.5'),
    ('x-small',     'knowledgator/gliner-x-small'),
    ('x-base',      'knowledgator/gliner-x-base'),
    ('x-large',     'knowledgator/gliner-x-large'),
]

results = []

for name, repo in MODELS:
    print(f'\n{"="*60}\nLoading {name} ({repo})...')
    try:
        model = GLiNER.from_pretrained(repo)
    except Exception as e:
        print(f'  FAILED: {e}')
        continue

    # CPU
    print(f'  CPU FP32...', end=' ', flush=True)
    for tc in TEST_CASES[:2]:
        model.predict_entities(tc['text'], tc['labels'], threshold=0.3)
    r, ms, lang = evaluate(model)
    results.append((name, 'CPU FP32', r, ms, lang))
    print(f'Recall={r:.1f}% {ms:.1f}ms')

    # MPS
    print(f'  MPS FP32...', end=' ', flush=True)
    try:
        model.to('mps')
        for tc in TEST_CASES[:2]:
            model.predict_entities(tc['text'], tc['labels'], threshold=0.3)
        r, ms, lang = evaluate(model)
        results.append((name, 'MPS FP32', r, ms, lang))
        print(f'Recall={r:.1f}% {ms:.1f}ms')
        model.to('cpu')
    except Exception as e:
        print(f'FAIL: {e}')
        results.append((name, 'MPS FP32', None, None, None))

    # ONNX - save then reload
    print(f'  ONNX FP32...', end=' ', flush=True)
    try:
        onnx_dir = f'/Users/fl/projets/GLiNER/models/{name}'
        os.makedirs(onnx_dir, exist_ok=True)
        model.save_pretrained(onnx_dir)
        del model; cleanup()
        onnx_model = GLiNER.from_pretrained(onnx_dir, load_onnx_model=True)
        for tc in TEST_CASES[:2]:
            onnx_model.predict_entities(tc['text'], tc['labels'], threshold=0.3)
        r, ms, lang = evaluate(onnx_model)
        results.append((name, 'ONNX FP32', r, ms, lang))
        print(f'Recall={r:.1f}% {ms:.1f}ms')
        del onnx_model
    except Exception as e:
        print(f'FAIL: {e}')
        results.append((name, 'ONNX FP32', None, None, None))
    cleanup()

# Threshold tuning
for tune_name, tune_repo in [('small-v2.5', 'gliner-community/gliner_small-v2.5'),
                              ('x-large', 'knowledgator/gliner-x-large')]:
    print(f'\n--- Threshold tuning: {tune_name} ---')
    try:
        model = GLiNER.from_pretrained(tune_repo)
        for th in [0.1, 0.2, 0.3, 0.4, 0.5]:
            r, ms, lang = evaluate(model, threshold=th)
            results.append((tune_name, f'CPU th={th}', r, ms, lang))
            print(f'  th={th}: Recall={r:.1f}%')
        del model; cleanup()
    except Exception as e:
        print(f'  FAIL: {e}')

# Final table
print('\n' + '='*120)
hdr = f"{'Model':<15}{'Backend':<15}{'Recall%':<9}{'ms/call':<9}" + ''.join(f"{l:<5}" for l in LANGS)
print(hdr)
print('-'*120)
for name, backend, r, ms, lang in results:
    if r is None:
        print(f"{name:<15}{backend:<15}{'FAIL':<9}")
        continue
    print(f"{name:<15}{backend:<15}{r:<9.1f}{ms:<9.1f}{lang_cols(lang)}")
print('='*120)
