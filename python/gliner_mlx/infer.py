"""GLiNER MLX inference via OpenMed."""
from huggingface_hub import snapshot_download
from openmed.mlx.inference import GLiNERRelexMLXPipeline

MODEL_REPO = "OpenMed/gliner-relex-base-v1.0-mlx"


def load_model(model_path: str | None = None) -> GLiNERRelexMLXPipeline:
    if model_path is None:
        model_path = snapshot_download(MODEL_REPO)
    return GLiNERRelexMLXPipeline(model_path)


def predict(pipeline: GLiNERRelexMLXPipeline, text: str,
            labels: list[str], relations: list[str],
            threshold: float = 0.5) -> dict:
    return pipeline.inference(text, labels=labels, relations=relations,
                              threshold=threshold)


if __name__ == "__main__":
    pipe = load_model()
    result = predict(
        pipe,
        "Steve Jobs co-founded Apple in Cupertino, California.",
        labels=["person", "organization", "location"],
        relations=["co-founded", "located in"],
    )
    print("Entities:")
    for e in result.get("entities", []):
        print(f"  {e['text']:20s} => {e['label']} ({e['score']:.3f})")
    print("Relations:")
    for r in result.get("relations", []):
        print(f"  {r['head']['text']} --[{r['label']}]--> {r['tail']['text']} ({r['score']:.3f})")
