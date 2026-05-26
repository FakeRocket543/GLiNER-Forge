/// gliner_wrapper.cpp — MLX C++ inference for GLiNER
/// Pattern follows dart-ml-forge/mlx/bert/src/ckip_bert.cpp
#include "gliner_wrapper.h"

#include <mlx/mlx.h>
#include <string>
#include <vector>
#include <memory>

namespace mx = mlx::core;

// ----- Internal model structure -----

struct GlinerModel_ {
    // TODO: load from safetensors
    // - DeBERTa-v3 encoder weights
    // - Span representation layer
    // - Classifier weights
    // - Tokenizer (sentencepiece or HF fast tokenizer)
    std::string model_dir;
};

// ----- C API implementation -----

extern "C" {

GlinerHandle gliner_load(const char *model_dir) {
    auto *model = new GlinerModel_();
    model->model_dir = model_dir;
    // TODO: load weights.safetensors via mx::load()
    // TODO: load tokenizer.json
    return model;
}

void gliner_free(GlinerHandle handle) {
    delete handle;
}

GlinerResult gliner_predict(GlinerHandle handle,
                            const char *text,
                            const char **labels, int num_labels,
                            float threshold) {
    GlinerResult result = {};
    // TODO: implement
    // 1. Tokenize: build schema "[P] entities ( [E] label1 [E] label2 ) [SEP_TEXT] text"
    // 2. Encoder forward: mDeBERTa-v3 disentangled attention
    // 3. Span representation: start/end hidden state concatenation
    // 4. Classifier: score spans against label embeddings
    // 5. Threshold + NMS → entities
    result.num_entities = 0;
    result.entities = nullptr;
    return result;
}

void gliner_result_free(GlinerResult *result) {
    if (result && result->entities) {
        for (int i = 0; i < result->num_entities; i++) {
            free((void *)result->entities[i].text);
            free((void *)result->entities[i].label);
        }
        free(result->entities);
        result->entities = nullptr;
    }
}

} // extern "C"
