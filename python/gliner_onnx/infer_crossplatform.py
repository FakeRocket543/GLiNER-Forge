"""
GLiNER ONNX inference — cross-platform (macOS + Linux ARM).

Supports: CoreML (macOS), CPUExecutionProvider (Linux/ARM/any)

Usage:
    python infer.py --model-dir ~/gliner-model --variant int8

Requirements:
    pip install onnxruntime tokenizers numpy
"""

import argparse
import os
import sys

import numpy as np
import onnxruntime as ort
from tokenizers import Tokenizer

# ── Platform detection ───────────────────────────────────────

def get_providers():
    """Return available ORT providers in priority order."""
    available = ort.get_available_providers()
    if "CoreMLExecutionProvider" in available:
        return ["CoreMLExecutionProvider", "CPUExecutionProvider"]
    return ["CPUExecutionProvider"]


# ── Model loading ────────────────────────────────────────────

class GLiNEROnnx:
    def __init__(self, model_dir: str, variant: str = "int8"):
        self.variant = variant
        self.model_dir = model_dir
        self.providers = get_providers()
        print(f"ORT providers: {self.providers}")

        # Locate model files
        suffix = f"_{variant}" if variant != "fp16" else "_fp16"
        enc_path = os.path.join(model_dir, variant, f"encoder{suffix}.onnx")
        tok_path = self._find_tokenizer(model_dir, variant)

        if not os.path.exists(enc_path):
            raise FileNotFoundError(f"Encoder not found: {enc_path}")

        opts = ort.SessionOptions()
        opts.graph_optimization_level = ort.GraphOptimizationLevel.ORT_ENABLE_ALL

        self.encoder = ort.InferenceSession(enc_path, opts, providers=self.providers)
        self.tokenizer = Tokenizer.from_file(tok_path)

        # Check encoder input spec
        inputs = self.encoder.get_inputs()
        self.needs_attention_mask = len(inputs) > 1 and "attention" in inputs[1].name
        print(f"Encoder inputs: {[i.name for i in inputs]}, attention_mask={self.needs_attention_mask}")

    def _find_tokenizer(self, model_dir: str, variant: str) -> str:
        """Find tokenizer.json in model directory tree."""
        candidates = [
            os.path.join(model_dir, variant, "tokenizer.json"),
            os.path.join(model_dir, "fp16", "tokenizer.json"),
            os.path.join(model_dir, "tokenizer.json"),
        ]
        for p in candidates:
            if os.path.exists(p):
                return p
        raise FileNotFoundError(f"tokenizer.json not found in {model_dir}")

    def predict(self, text: str, labels: list[str], threshold: float = 0.5,
                max_len: int = 512) -> dict:
        """Run encoder and return hidden states for downstream NER."""
        # Build GLiNER input
        schema = " ".join(f"[E] {l}" for l in labels)
        full_input = f"[P] entities ( {schema} ) [SEP_TEXT] {text}"

        encoded = self.tokenizer.encode(full_input)
        ids = encoded.ids + [0] * (max_len - len(encoded.ids))
        mask = encoded.attention_mask + [0] * (max_len - len(encoded.attention_mask))

        input_ids = np.array([ids], dtype=np.int64)
        n_tokens = sum(m for m in encoded.attention_mask)

        import time
        t0 = time.time()

        feed = {"input_ids": input_ids}
        if self.needs_attention_mask:
            feed["attention_mask"] = np.array([mask], dtype=np.int64)

        hidden = self.encoder.run(None, feed)[0]
        elapsed = (time.time() - t0) * 1000

        return {
            "hidden": hidden,
            "n_tokens": n_tokens,
            "elapsed_ms": elapsed,
            "hidden_shape": hidden.shape,
        }


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--model-dir", default=os.path.expanduser("~/gliner-model"))
    parser.add_argument("--variant", default="int8", choices=["fp16", "fp32", "int8"])
    parser.add_argument("--text", default="Tim Cook is the CEO of Apple in Cupertino.")
    parser.add_argument("--labels", nargs="+", default=["person", "organization", "location"])
    args = parser.parse_args()

    model = GLiNEROnnx(args.model_dir, variant=args.variant)
    result = model.predict(args.text, args.labels)
    print(f"\nInput tokens: {result['n_tokens']}")
    print(f"Encoder time: {result['elapsed_ms']:.0f}ms")
    print(f"Hidden shape: {result['hidden_shape']}")
