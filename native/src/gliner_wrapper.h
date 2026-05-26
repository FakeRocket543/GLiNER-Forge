/// gliner_wrapper.h — C API for GLiNER NER via ONNX Runtime
///
/// Usage:
///   GlinerHandle h = gliner_load("models/small-v2.5");
///   GlinerResult r = gliner_predict(h, "Tim Cook is CEO of Apple", labels, 3, 0.3);
///   // use r.entities[0..r.num_entities]
///   gliner_result_free(&r);
///   gliner_free(h);
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
    int32_t start;  // char offset
    int32_t end;    // char offset
} GlinerEntity;

typedef struct {
    GlinerEntity *entities;
    int32_t num_entities;
    int32_t error_code;       // 0 = success
    const char *error_msg;    // NULL if no error
} GlinerResult;

/// Load model from directory containing model.onnx, tokenizer.json, gliner_config.json.
GlinerHandle gliner_load(const char *model_dir);

/// Free model resources.
void gliner_free(GlinerHandle handle);

/// Run NER prediction.
/// labels: array of label strings, num_labels: count
/// threshold: confidence threshold (0.0-1.0)
GlinerResult gliner_predict(GlinerHandle handle,
                            const char *text,
                            const char **labels, int32_t num_labels,
                            float threshold);

/// Free prediction result.
void gliner_result_free(GlinerResult *result);

/// Get version string.
const char *gliner_version(void);

#ifdef __cplusplus
}
#endif
#endif // GLINER_WRAPPER_H
