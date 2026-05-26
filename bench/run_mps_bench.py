"""MPS (Metal) backend benchmark for GLiNER on Apple Silicon."""
import sys
import time
sys.path.insert(0, '/Users/fl/projets/GLiNER/bench')

import torch
from gliner import GLiNER
from test_data_taiwan import TEST_CASES

WARMUP = 2
TIMED = 5
MODEL_NAME = 'gliner-community/gliner_small-v2.5'

print(f"PyTorch version: {torch.__version__}")
print(f"MPS available: {torch.backends.mps.is_available()}")
print(f"MPS built: {torch.backends.mps.is_built()}")
print(f"Test cases: {len(TEST_CASES)}")
print("=" * 70)

# Load model
print("\nLoading model...")
model = GLiNER.from_pretrained(MODEL_NAME)
print(f"Model type: {type(model)}")
print(f"Has .to(): {hasattr(model, 'to')}")
print(f"Has .model: {hasattr(model, 'model')}")
if hasattr(model, 'device'):
    print(f"model.device: {model.device}")

def run_predict(model, label=""):
    """Run predict_entities on all test cases, return total time."""
    for tc in TEST_CASES:
        model.predict_entities(tc["text"], tc["labels"], threshold=0.3)

def benchmark(model, config_name):
    """Warmup + timed runs, return avg time."""
    print(f"\n--- {config_name} ---")
    # Warmup
    for i in range(WARMUP):
        try:
            run_predict(model)
            print(f"  warmup {i+1}/{WARMUP} ok")
        except Exception as e:
            print(f"  warmup {i+1}/{WARMUP} FAILED: {e}")
            return None
    # Timed
    times = []
    for i in range(TIMED):
        t0 = time.perf_counter()
        run_predict(model)
        if torch.backends.mps.is_available():
            torch.mps.synchronize()
        elapsed = time.perf_counter() - t0
        times.append(elapsed)
        print(f"  run {i+1}/{TIMED}: {elapsed:.3f}s")
    avg = sum(times) / len(times)
    print(f"  AVG: {avg:.3f}s")
    return avg

results = {}

# --- 1. CPU FP32 ---
model_cpu = GLiNER.from_pretrained(MODEL_NAME)
results['CPU FP32'] = benchmark(model_cpu, 'CPU FP32')

# --- 2. MPS FP32 ---
print("\n\n=== Attempting MPS FP32 ===")
model_mps = GLiNER.from_pretrained(MODEL_NAME)

# Try model.to('mps')
mps_ok = False
try:
    model_mps.to('mps')
    print("model.to('mps') worked")
    mps_ok = True
except Exception as e:
    print(f"model.to('mps') failed: {e}")
    # Try model.model.to('mps')
    try:
        model_mps.model.to('mps')
        print("model.model.to('mps') worked")
        mps_ok = True
    except Exception as e2:
        print(f"model.model.to('mps') failed: {e2}")

if mps_ok:
    # Try a single predict first
    try:
        r = model_mps.predict_entities('TSMC is in Taiwan', ['organization', 'location'], threshold=0.3)
        print(f"MPS FP32 predict test: {r}")
        results['MPS FP32'] = benchmark(model_mps, 'MPS FP32')
    except Exception as e:
        print(f"MPS FP32 predict FAILED: {e}")
        # Try setting device attribute
        print("Trying model.device = torch.device('mps')...")
        try:
            model_mps.device = torch.device('mps')
            r = model_mps.predict_entities('TSMC is in Taiwan', ['organization', 'location'], threshold=0.3)
            print(f"MPS FP32 predict with device attr: {r}")
            results['MPS FP32'] = benchmark(model_mps, 'MPS FP32')
        except Exception as e2:
            print(f"MPS FP32 predict still FAILED: {e2}")
            results['MPS FP32'] = None
else:
    results['MPS FP32'] = None

# --- 3. MPS FP16 ---
print("\n\n=== Attempting MPS FP16 ===")
model_fp16 = GLiNER.from_pretrained(MODEL_NAME)

fp16_ok = False
try:
    model_fp16.to(device='mps', dtype=torch.float16)
    print("model.to(device='mps', dtype=float16) worked")
    fp16_ok = True
except Exception as e:
    print(f"model.to(device='mps', dtype=float16) failed: {e}")
    try:
        model_fp16.model.to(device='mps', dtype=torch.float16)
        print("model.model.to(device='mps', dtype=float16) worked")
        fp16_ok = True
    except Exception as e2:
        print(f"model.model.to(device='mps', dtype=float16) failed: {e2}")

if fp16_ok:
    try:
        r = model_fp16.predict_entities('TSMC is in Taiwan', ['organization', 'location'], threshold=0.3)
        print(f"MPS FP16 predict test: {r}")
        results['MPS FP16'] = benchmark(model_fp16, 'MPS FP16')
    except Exception as e:
        print(f"MPS FP16 predict FAILED: {e}")
        print("Trying model.device = torch.device('mps')...")
        try:
            model_fp16.device = torch.device('mps')
            r = model_fp16.predict_entities('TSMC is in Taiwan', ['organization', 'location'], threshold=0.3)
            print(f"MPS FP16 predict with device attr: {r}")
            results['MPS FP16'] = benchmark(model_fp16, 'MPS FP16')
        except Exception as e2:
            print(f"MPS FP16 predict still FAILED: {e2}")
            results['MPS FP16'] = None
else:
    results['MPS FP16'] = None

# --- 4. ONNX FP32 (if available) ---
print("\n\n=== Attempting ONNX FP32 ===")
try:
    from gliner import GLiNER as GLiNER_ONNX
    model_onnx = GLiNER_ONNX.from_pretrained(MODEL_NAME, load_onnx_model=True)
    # Test
    r = model_onnx.predict_entities('TSMC is in Taiwan', ['organization', 'location'], threshold=0.3)
    print(f"ONNX predict test: {r}")
    results['ONNX FP32'] = benchmark(model_onnx, 'ONNX FP32')
except Exception as e:
    print(f"ONNX not available: {e}")
    results['ONNX FP32'] = None

# --- Results Table ---
print("\n\n" + "=" * 70)
print(f"{'Config':<20} {'Avg Time (s)':<15} {'Speedup vs CPU':<15}")
print("-" * 70)
cpu_time = results.get('CPU FP32')
for cfg, t in results.items():
    if t is not None:
        speedup = f"{cpu_time/t:.2f}x" if cpu_time else "N/A"
        print(f"{cfg:<20} {t:<15.3f} {speedup:<15}")
    else:
        print(f"{cfg:<20} {'FAILED':<15} {'N/A':<15}")
print("=" * 70)
