/// test_main.cpp — Quick smoke test for gliner C API
#include "gliner_wrapper.h"
#include <cstdio>
#include <cstdlib>

int main(int argc, char **argv) {
    const char *model_dir = argc > 1 ? argv[1] : "../models/small-v2.5";
    float threshold = 0.3f;

    printf("GLiNER C++ wrapper v%s\n", gliner_version());
    printf("Loading model: %s\n", model_dir);

    GlinerHandle h = gliner_load(model_dir);
    if (!h) {
        fprintf(stderr, "ERROR: failed to load model\n");
        return 1;
    }

    const char *text = "Tim Cook is the CEO of Apple in Cupertino, California.";
    const char *labels[] = {"person", "organization", "location"};
    int num_labels = 3;

    printf("Text: %s\n", text);
    printf("Labels: person, organization, location\n");
    printf("Threshold: %.2f\n\n", threshold);

    GlinerResult r = gliner_predict(h, text, labels, num_labels, threshold);

    if (r.error_code) {
        fprintf(stderr, "ERROR [%d]: %s\n", r.error_code, r.error_msg ? r.error_msg : "unknown");
        gliner_free(h);
        return 1;
    }

    printf("Entities found: %d\n", r.num_entities);
    for (int i = 0; i < r.num_entities; i++) {
        printf("  %-20s → %-15s (%.3f) [%d:%d]\n",
               r.entities[i].text, r.entities[i].label,
               r.entities[i].score, r.entities[i].start, r.entities[i].end);
    }

    gliner_result_free(&r);
    gliner_free(h);
    printf("\nDone.\n");
    return 0;
}
