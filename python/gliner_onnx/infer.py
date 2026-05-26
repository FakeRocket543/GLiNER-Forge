"""GLiNER ONNX inference via onnxruntime."""
import numpy as np
import onnxruntime as ort
from transformers import AutoTokenizer

MODEL_REPO = "SemplificaAI/gliner2-multi-v1-onnx"
REVISION = "main"
VARIANT = "fp16"


class GLiNEROnnx:
    def __init__(self, model_dir: str, variant: str = VARIANT):
        opts = ort.SessionOptions()
        providers = ["CoreMLExecutionProvider", "CPUExecutionProvider"]
        self.encoder = ort.InferenceSession(
            f"{model_dir}/{variant}/encoder.onnx", opts, providers=providers)
        self.span_rep = ort.InferenceSession(
            f"{model_dir}/{variant}/span_rep.onnx", opts, providers=providers)
        self.classifier = ort.InferenceSession(
            f"{model_dir}/{variant}/classifier.onnx", opts, providers=providers)
        self.tokenizer = AutoTokenizer.from_pretrained(model_dir)

    def predict(self, text: str, labels: list[str], threshold: float = 0.5) -> list[dict]:
        # Build schema input: [P] entities ( [E] label1 [E] label2 ) [SEP_TEXT] text
        schema = " ".join(f"[E] {l}" for l in labels)
        full_input = f"[P] entities ( {schema} ) [SEP_TEXT] {text}"

        enc = self.tokenizer(full_input, return_tensors="np", padding=True)
        input_ids = enc["input_ids"].astype(np.int64)
        attention_mask = enc["attention_mask"].astype(np.int64)

        # Encoder
        hidden = self.encoder.run(None, {
            "input_ids": input_ids,
            "attention_mask": attention_mask,
        })[0]

        # TODO: span generation + classification
        # Full pipeline requires span index generation matching the model's schema
        print(f"Encoder output shape: {hidden.shape}")
        print("NOTE: Full span scoring pipeline TBD — use gliner2-rs or openmed for now")
        return []


if __name__ == "__main__":
    from huggingface_hub import snapshot_download
    model_dir = snapshot_download(MODEL_REPO, revision=REVISION)
    model = GLiNEROnnx(model_dir)
    model.predict(
        "Tim Cook is the CEO of Apple in Cupertino.",
        labels=["person", "organization", "location"],
    )
