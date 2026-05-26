"""Quantize GLiNER ONNX model (INT8 dynamic quantization)."""
import argparse
from pathlib import Path
from onnxruntime.quantization import quantize_dynamic, QuantType


def quantize_onnx(input_path: Path, output_path: Path, quant_type: str = "int8"):
    qtype = QuantType.QInt8 if quant_type == "int8" else QuantType.QUInt8
    quantize_dynamic(
        str(input_path), str(output_path),
        weight_type=qtype,
    )
    input_size = input_path.stat().st_size / 1024 / 1024
    output_size = output_path.stat().st_size / 1024 / 1024
    print(f"{input_path.name}: {input_size:.1f}MB → {output_size:.1f}MB ({output_size/input_size:.0%})")


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", required=True, help="Input .onnx file")
    parser.add_argument("--output", help="Output path (default: input_int8.onnx)")
    parser.add_argument("--type", choices=["int8", "uint8"], default="int8")
    args = parser.parse_args()

    input_path = Path(args.input)
    output_path = Path(args.output) if args.output else input_path.with_stem(f"{input_path.stem}_int8")

    quantize_onnx(input_path, output_path, args.type)


if __name__ == "__main__":
    main()
