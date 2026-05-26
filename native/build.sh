#!/bin/bash
# Build GLiNER MLX native wrapper
# Requires: MLX C++ headers + libmlx.a from dart-ml-forge/mlx/shared/build
set -e

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
MLX_SHARED="${HOME}/Python/dart-ml-forge/mlx/shared"
MLX_BUILD="${MLX_SHARED}/build"

if [ ! -f "${MLX_BUILD}/lib/libmlx.a" ]; then
    echo "ERROR: libmlx.a not found. Build mlx/shared first:"
    echo "  cd ${MLX_SHARED} && ./build.sh"
    exit 1
fi

echo "Building libgliner_wrapper.dylib..."
clang++ -std=c++17 -O2 -shared -fPIC \
    -I"${MLX_BUILD}/include" \
    -I"${MLX_SHARED}/mlx-c/include" \
    -L"${MLX_BUILD}/lib" \
    -lmlx -framework Metal -framework Foundation -framework Accelerate \
    -o "${SCRIPT_DIR}/../dist/libgliner_wrapper.dylib" \
    "${SCRIPT_DIR}/src/gliner_wrapper.cpp"

echo "Done → dist/libgliner_wrapper.dylib"
