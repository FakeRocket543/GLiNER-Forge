/// bench_main.cpp — Batch NER benchmark for gliner C API
/// Usage: ./bench_gliner <model_dir> [threshold]
/// Reads test cases from stdin as JSON lines: {"text":"...","labels":["a","b"]}
/// Outputs JSON lines: {"text":"...","entities":[{"text":"...","label":"...","score":0.9}]}

#include "gliner_wrapper.h"
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <iostream>
#include <string>
#include <vector>
#include <chrono>

// Minimal JSON parsing (no dependency)
static std::string json_get_string(const std::string &json, const std::string &key) {
    std::string needle = "\"" + key + "\"";
    auto pos = json.find(needle);
    if (pos == std::string::npos) return "";
    pos = json.find('"', pos + needle.size() + 1);
    if (pos == std::string::npos) return "";
    auto end = pos + 1;
    while (end < json.size() && json[end] != '"') {
        if (json[end] == '\\') end++;
        end++;
    }
    return json.substr(pos + 1, end - pos - 1);
}

static std::vector<std::string> json_get_string_array(const std::string &json, const std::string &key) {
    std::vector<std::string> result;
    std::string needle = "\"" + key + "\"";
    auto pos = json.find(needle);
    if (pos == std::string::npos) return result;
    pos = json.find('[', pos);
    if (pos == std::string::npos) return result;
    pos++;
    while (pos < json.size() && json[pos] != ']') {
        if (json[pos] == '"') {
            auto end = pos + 1;
            while (end < json.size() && json[end] != '"') {
                if (json[end] == '\\') end++;
                end++;
            }
            result.push_back(json.substr(pos + 1, end - pos - 1));
            pos = end + 1;
        } else {
            pos++;
        }
    }
    return result;
}

int main(int argc, char **argv) {
    const char *model_dir = argc > 1 ? argv[1] : "../models/small-v2.5";
    float threshold = argc > 2 ? atof(argv[2]) : 0.3f;

    GlinerHandle h = gliner_load(model_dir);
    if (!h) {
        fprintf(stderr, "{\"error\":\"failed to load model: %s\"}\n", model_dir);
        return 1;
    }

    std::string line;
    int total = 0;
    double total_ms = 0;

    while (std::getline(std::cin, line)) {
        if (line.empty()) continue;

        std::string text = json_get_string(line, "text");
        auto labels = json_get_string_array(line, "labels");
        if (text.empty() || labels.empty()) continue;

        std::vector<const char *> label_ptrs;
        for (auto &l : labels) label_ptrs.push_back(l.c_str());

        auto t0 = std::chrono::high_resolution_clock::now();
        GlinerResult r = gliner_predict(h, text.c_str(), label_ptrs.data(), (int)label_ptrs.size(), threshold);
        auto t1 = std::chrono::high_resolution_clock::now();
        double ms = std::chrono::duration<double, std::milli>(t1 - t0).count();
        total_ms += ms;
        total++;

        // Output JSON — escape text for valid JSON
        printf("{\"entities\":[");
        for (int i = 0; i < r.num_entities; i++) {
            if (i > 0) printf(",");
            printf("{\"text\":\"%s\",\"label\":\"%s\",\"score\":%.4f}",
                   r.entities[i].text, r.entities[i].label, r.entities[i].score);
        }
        printf("],\"latency_ms\":%.1f}\n", ms);
        fflush(stdout);

        gliner_result_free(&r);
    }

    fprintf(stderr, "Processed %d cases, avg %.1fms/case\n", total, total > 0 ? total_ms / total : 0);
    gliner_free(h);
    return 0;
}
