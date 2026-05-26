"""
Fix fp16 remnants in ONNX models before quantization.

Problem: ONNX models exported with fp16 weights contain fp16 tensors in
three hidden locations that survive simple initializer conversion:
  1. Constant node `value` attributes
  2. ConstantOfShape node `value` attributes
  3. Cast nodes targeting FLOAT16

ORT's `quantize_dynamic` will fail with type errors if any fp16 remains.

Usage:
    python fix_fp16.py input.onnx output.onnx [--verify]

Requirements: pip install onnx numpy
"""

import argparse
from pathlib import Path

import numpy as np
import onnx
from onnx import AttributeProto, TensorProto, numpy_helper


def fix_fp16_model(input_path: str, output_path: str, verify: bool = False) -> int:
    """Convert ALL fp16 tensors in an ONNX model to fp32. Returns count of fixed tensors."""
    model = onnx.load(input_path)
    fixed = 0

    # 1. Graph initializers (weights)
    for init in model.graph.initializer:
        if init.data_type == TensorProto.FLOAT16:
            arr = numpy_helper.to_array(init).astype(np.float32)
            init.CopyFrom(numpy_helper.from_array(arr, name=init.name))
            fixed += 1

    # 2. ALL node tensor attributes (Constant, ConstantOfShape, etc.)
    for node in model.graph.node:
        for attr in node.attribute:
            if attr.type == AttributeProto.TENSOR and attr.t.data_type == TensorProto.FLOAT16:
                arr = numpy_helper.to_array(attr.t).astype(np.float32)
                attr.t.CopyFrom(numpy_helper.from_array(arr, name=attr.t.name))
                fixed += 1

        # 3. Cast nodes targeting fp16
        if node.op_type == "Cast":
            for attr in node.attribute:
                if attr.name == "to" and attr.i == TensorProto.FLOAT16:
                    attr.i = TensorProto.FLOAT
                    fixed += 1

    # 4. value_info, input, output type annotations
    for container in [model.graph.value_info, model.graph.input, model.graph.output]:
        for item in container:
            tt = item.type.tensor_type
            if tt.elem_type == TensorProto.FLOAT16:
                tt.elem_type = TensorProto.FLOAT

    # Verify no fp16 remains
    if verify:
        remaining = 0
        for init in model.graph.initializer:
            if init.data_type == TensorProto.FLOAT16:
                remaining += 1
        for node in model.graph.node:
            for attr in node.attribute:
                if attr.type == AttributeProto.TENSOR and attr.t.data_type == TensorProto.FLOAT16:
                    remaining += 1
        if remaining > 0:
            print(f"⚠️  WARNING: {remaining} fp16 tensors still remain!")
        else:
            print("✅ Verified: 0 fp16 tensors remain")

    onnx.save(model, output_path)
    return fixed


def main():
    parser = argparse.ArgumentParser(description="Fix fp16 remnants in ONNX model")
    parser.add_argument("input", help="Input ONNX file")
    parser.add_argument("output", help="Output ONNX file (fp32)")
    parser.add_argument("--verify", action="store_true", help="Verify no fp16 remains")
    args = parser.parse_args()

    import os
    in_size = os.path.getsize(args.input) / 1024 / 1024
    print(f"Converting {args.input} ({in_size:.0f}MB)...")

    fixed = fix_fp16_model(args.input, args.output, args.verify)

    out_size = os.path.getsize(args.output) / 1024 / 1024
    print(f"Fixed {fixed} fp16 tensors → {args.output} ({out_size:.0f}MB)")


if __name__ == "__main__":
    main()
