"""Convert GLiNER PyTorch weights to MLX safetensors format."""
import argparse
from pathlib import Path
import numpy as np

import mlx.core as mx
from safetensors.torch import load_file as load_torch_st
from safetensors.numpy import save_file as save_np_st


def convert_weights(src_dir: Path, dst_dir: Path):
    dst_dir.mkdir(parents=True, exist_ok=True)
    st_files = list(src_dir.glob("*.safetensors"))
    if not st_files:
        raise FileNotFoundError(f"No safetensors found in {src_dir}")

    all_tensors = {}
    for f in st_files:
        tensors = load_torch_st(str(f))
        for k, v in tensors.items():
            all_tensors[k] = v.numpy().astype(np.float16)

    save_np_st(all_tensors, str(dst_dir / "weights.safetensors"))
    print(f"Saved {len(all_tensors)} tensors → {dst_dir / 'weights.safetensors'}")


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--src", required=True, help="PyTorch model dir with .safetensors")
    parser.add_argument("--dst", default="models/mlx", help="Output MLX dir")
    args = parser.parse_args()
    convert_weights(Path(args.src), Path(args.dst))


if __name__ == "__main__":
    main()
