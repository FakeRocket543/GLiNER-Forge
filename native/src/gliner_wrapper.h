/// gliner_wrapper.h — C API for GLiNER (NER + RE) via MLX
#ifndef GLINER_WRAPPER_H
#define GLINER_WRAPPER_H

#include <stddef.h>
#include <stdint.h>

#ifdef __cplusplus
extern "C" {
#endif

typedef struct GlinerModel_ *GlinerHandle;

typedef struct {
    const char *text;
    const char *label;
    float score;
    int start;
    int end;
} GlinerEntity;

typedef struct {
    GlinerEntity *entities;
    int num_entities;
    int32_t error_code;
    const char *error_msg;
} GlinerResult;

/// Load model from MLX safetensors directory.
/// model_dir should contain weights.safetensors, config.json, tokenizer.json
GlinerHandle gliner_load(const char *model_dir);
void gliner_free(GlinerHandle handle);

/// Run NER on text with given entity labels.
/// labels: null-terminated array of label strings
/// threshold: confidence threshold (0.0-1.0)
GlinerResult gliner_predict(GlinerHandle handle,
                            const char *text,
                            const char **labels, int num_labels,
                            float threshold);
void gliner_result_free(GlinerResult *result);

#ifdef __cplusplus
}
#endif
#endif
