#!/bin/bash
# Build GLiNER native wrapper (ONNX Runtime + tokenizers-cpp)
#
# Prerequisites:
#   brew install onnxruntime
#   # tokenizers-cpp: clone & build mlc-ai/tokenizers-cpp
#
# Usage:
#   ./build.sh              # build with real tokenizer (default)
#   ./build.sh --stub       # build with stub tokenizer (compile-only testing)

set -e
cd "$(dirname "$0")"

ONNXRT_PREFIX="${ONNXRUNTIME_DIR:-/opt/homebrew}"
TOKENIZERS_DIR="${TOKENIZERS_CPP_DIR:-$(pwd)/tokenizers-cpp}"
USE_STUB=0

if [[ "$1" == "--stub" ]]; then
    USE_STUB=1
fi

echo "=== Building gliner_wrapper ==="
echo "  ONNX Runtime: ${ONNXRT_PREFIX}"

if [[ $USE_STUB -eq 1 ]]; then
    echo "  Tokenizer:    STUB (no real inference)"
    TOK_SRC="src/tokenizer_stub.cpp"
    TOK_FLAGS=""
else
    echo "  Tokenizer:    tokenizers-cpp @ ${TOKENIZERS_DIR}"
    TOK_SRC="src/hf_tokenizer.cpp"
    TOK_FLAGS="-I ${TOKENIZERS_DIR}/include -L ${TOKENIZERS_DIR}/build -ltokenizers_cpp -ltokenizers_c"

    if [[ ! -d "${TOKENIZERS_DIR}" ]]; then
        echo ""
        echo "ERROR: tokenizers-cpp not found at ${TOKENIZERS_DIR}"
        echo "  git clone https://github.com/mlc-ai/tokenizers-cpp.git"
        echo "  cd tokenizers-cpp && mkdir build && cd build && cmake .. && make -j"
        echo ""
        echo "Or set TOKENIZERS_CPP_DIR=/path/to/tokenizers-cpp"
        echo "Or use: ./build.sh --stub"
        exit 1
    fi
fi

clang++ -std=c++17 -O2 -shared -fPIC \
    -I "${ONNXRT_PREFIX}/include" \
    -I "${ONNXRT_PREFIX}/include/onnxruntime" \
    -L "${ONNXRT_PREFIX}/lib" \
    -lonnxruntime \
    ${TOK_FLAGS} \
    -o libgliner.dylib \
    src/gliner_wrapper.cpp \
    ${TOK_SRC}

echo "=== Built: libgliner.dylib ==="

# Also build test binary if main exists
if [[ -f src/test_main.cpp ]]; then
    echo "=== Building test binary ==="
    clang++ -std=c++17 -O2 \
        -I "${ONNXRT_PREFIX}/include" \
        -I "${ONNXRT_PREFIX}/include/onnxruntime" \
        -L "${ONNXRT_PREFIX}/lib" \
        -L "$(pwd)" \
        -lonnxruntime -lgliner \
        ${TOK_FLAGS} \
        -o test_gliner \
        src/test_main.cpp
    echo "=== Built: test_gliner ==="
fi
