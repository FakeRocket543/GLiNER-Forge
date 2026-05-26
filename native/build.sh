#!/bin/bash
# Build GLiNER native wrapper (ONNX Runtime + tokenizers-cpp)
#
# Prerequisites:
#   brew install onnxruntime
#   # Or download from https://github.com/microsoft/onnxruntime/releases
#
# Tokenizer dependency (pick one):
#   - tokenizers-cpp: https://github.com/pijyoi/tokenizers_cpp
#   - Or link against HuggingFace tokenizers Rust lib via C FFI

set -e
cd "$(dirname "$0")"

ONNXRT_PREFIX="${ONNXRUNTIME_DIR:-/opt/homebrew}"
TOKENIZERS_DIR="${TOKENIZERS_CPP_DIR:-/opt/homebrew}"

echo "=== Building gliner_wrapper ==="
echo "  ONNX Runtime: ${ONNXRT_PREFIX}"
echo "  Tokenizers:   ${TOKENIZERS_DIR}"

# Compile (stub tokenizer for now — replace with real impl)
clang++ -std=c++17 -O2 -shared -fPIC \
    -I "${ONNXRT_PREFIX}/include" \
    -I "${ONNXRT_PREFIX}/include/onnxruntime" \
    -I "${TOKENIZERS_DIR}/include" \
    -L "${ONNXRT_PREFIX}/lib" \
    -L "${TOKENIZERS_DIR}/lib" \
    -lonnxruntime \
    -o libgliner.dylib \
    src/gliner_wrapper.cpp \
    src/tokenizer_stub.cpp

echo "=== Built: libgliner.dylib ==="
echo ""
echo "Remaining TODO:"
echo "  - Implement src/tokenizer_stub.cpp with real HF tokenizer"
echo "  - Or link tokenizers-cpp / sentencepiece"
