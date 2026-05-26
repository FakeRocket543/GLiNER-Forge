"""Export GLiNER2 PyTorch model to ONNX (fragmented)."""
import argparse
from pathlib import Path
import torch
from gliner import GLiNER


def export_encoder(model, save_dir: Path, opset: int = 17):
    encoder = model.model.token_rep_layer.bert_layer
    dummy_ids = torch.randint(0, 1000, (1, 128))
    dummy_mask = torch.ones(1, 128, dtype=torch.long)

    torch.onnx.export(
        encoder, (dummy_ids, dummy_mask),
        str(save_dir / "encoder.onnx"),
        input_names=["input_ids", "attention_mask"],
        output_names=["hidden_state"],
        dynamic_axes={"input_ids": {0: "batch", 1: "seq"},
                      "attention_mask": {0: "batch", 1: "seq"},
                      "hidden_state": {0: "batch", 1: "seq"}},
        opset_version=opset,
    )
    print(f"Exported encoder → {save_dir / 'encoder.onnx'}")


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--model", default="urchade/gliner_medium-v2.1")
    parser.add_argument("--output", default="models/onnx")
    parser.add_argument("--opset", type=int, default=17)
    args = parser.parse_args()

    save_dir = Path(args.output)
    save_dir.mkdir(parents=True, exist_ok=True)

    print(f"Loading {args.model}...")
    model = GLiNER.from_pretrained(args.model)
    model.eval()

    export_encoder(model, save_dir, args.opset)
    # TODO: export span_rep, classifier, count_pred
    print("NOTE: Full fragmented export — refer to dx111ge/gliner2-multi-v1-onnx export script")


if __name__ == "__main__":
    main()
