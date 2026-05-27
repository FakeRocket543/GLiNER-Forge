/// gliner_wrapper.cpp — GLiNER ONNX Runtime inference (C++ impl, C API)
///
/// Architecture: same pipeline as python/gliner_onnx/infer.py
///   1. Split text into words (regex: \w+(?:[-_]\w+)*|\S)
///   2. Build prompt: <<ENT>> label1 <<ENT>> label2 <<SEP>> word1 word2 ...
///   3. Tokenize with HF tokenizer (via tokenizers-cpp or sentencepiece)
///   4. Build words_mask, text_lengths, span_idx, span_mask
///   5. Run ONNX session → logits (L, K, C)
///   6. Sigmoid → threshold → greedy NMS → entities
///
/// Dependencies:
///   - onnxruntime (C API)
///   - tokenizers-cpp (HuggingFace tokenizer, from tokenizers.json)
///   - nlohmann/json (config parsing)

#include "gliner_wrapper.h"
#include <onnxruntime_c_api.h>

#include <cmath>
#include <cstring>
#include <fstream>
#include <memory>
#include <string>
#include <vector>

// Forward declarations for tokenizer (implementation-defined)
struct HFTokenizer;
extern "C" HFTokenizer *hf_tokenizer_load(const char *tokenizer_json_path);
extern "C" void hf_tokenizer_free(HFTokenizer *tok);

struct TokenizeResult {
    std::vector<int64_t> input_ids;
    std::vector<int64_t> attention_mask;
    std::vector<int> word_ids;  // -1 for special tokens
};
TokenizeResult hf_tokenize(HFTokenizer *tok, const std::vector<std::string> &words);

// ─── Internal model state ───

struct GlinerModel_ {
    OrtEnv *env = nullptr;
    OrtSession *session = nullptr;
    OrtSessionOptions *opts = nullptr;
    HFTokenizer *tokenizer = nullptr;

    int max_width = 12;
    std::string ent_token = "<<ENT>>";
    std::string sep_token = "<<SEP>>";
    std::string model_dir;

    ~GlinerModel_() {
        const OrtApi *api = OrtGetApiBase()->GetApi(ORT_API_VERSION);
        if (session) api->ReleaseSession(session);
        if (opts) api->ReleaseSessionOptions(opts);
        if (env) api->ReleaseEnv(env);
        if (tokenizer) hf_tokenizer_free(tokenizer);
    }
};

// ─── Helpers ───

struct Word {
    std::string text;
    int start;
    int end;
};

// Check if a UTF-8 codepoint is a CJK ideograph (should be split per-char)
static bool is_cjk(int cp) {
    return (cp >= 0x4E00 && cp <= 0x9FFF) || (cp >= 0x3400 && cp <= 0x4DBF) ||
           (cp >= 0xF900 && cp <= 0xFAFF) || (cp >= 0x3040 && cp <= 0x30FF);
}

// Decode one UTF-8 character, return codepoint and advance index
static int utf8_decode(const std::string &s, int &i) {
    unsigned char c = s[i];
    int cp, len;
    if (c < 0x80) { cp = c; len = 1; }
    else if ((c & 0xE0) == 0xC0) { cp = c & 0x1F; len = 2; }
    else if ((c & 0xF0) == 0xE0) { cp = c & 0x0F; len = 3; }
    else { cp = c & 0x07; len = 4; }
    for (int j = 1; j < len && i + j < (int)s.size(); j++)
        cp = (cp << 6) | (s[i + j] & 0x3F);
    i += len;
    return cp;
}

// Check if codepoint is an alphabetic character (non-CJK, non-digit, non-punct)
static bool is_alpha(int cp) {
    if (cp >= 'a' && cp <= 'z') return true;
    if (cp >= 'A' && cp <= 'Z') return true;
    // Latin Extended, Cyrillic, Greek, Arabic, Thai, Devanagari, etc.
    if (cp >= 0x00C0 && cp <= 0x024F) return true;  // Latin Extended
    if (cp >= 0x0400 && cp <= 0x04FF) return true;  // Cyrillic
    if (cp >= 0x0370 && cp <= 0x03FF) return true;  // Greek
    if (cp >= 0x0600 && cp <= 0x06FF) return true;  // Arabic
    if (cp >= 0x0900 && cp <= 0x097F) return true;  // Devanagari
    if (cp >= 0x0E00 && cp <= 0x0E7F) return true;  // Thai
    if (cp >= 0x1E00 && cp <= 0x1EFF) return true;  // Latin Extended Additional (Vietnamese)
    if (cp >= 0xAC00 && cp <= 0xD7AF) return true;  // Hangul Syllables
    if (cp >= 0x1100 && cp <= 0x11FF) return true;  // Hangul Jamo
    return false;
}

static int utf8_char_len(unsigned char c) {
    if (c < 0x80) return 1;
    if ((c & 0xE0) == 0xC0) return 2;
    if ((c & 0xF0) == 0xE0) return 3;
    return 4;
}

static std::vector<Word> split_words(const std::string &text) {
    std::vector<Word> words;
    int i = 0, len = (int)text.size();
    while (i < len) {
        unsigned char c = text[i];
        // Skip whitespace
        if (c == ' ' || c == '\t' || c == '\n' || c == '\r') { i++; continue; }

        int start = i;
        int cp_i = i;
        int cp = utf8_decode(text, cp_i);

        // CJK/Kana: single character per word
        if (is_cjk(cp)) {
            words.push_back({text.substr(start, cp_i - start), start, cp_i});
            i = cp_i;
            continue;
        }

        // Alphabetic: consume entire word
        if (is_alpha(cp)) {
            i = cp_i;
            while (i < len) {
                int next_i = i;
                int next_cp = utf8_decode(text, next_i);
                if (is_alpha(next_cp) || next_cp == '-' || next_cp == '_') {
                    i = next_i;
                } else break;
            }
            words.push_back({text.substr(start, i - start), start, i});
            continue;
        }

        // Digits
        if (cp >= '0' && cp <= '9') {
            while (i < len && text[i] >= '0' && text[i] <= '9') i++;
            words.push_back({text.substr(start, i - start), start, i});
            continue;
        }

        // Any other single character
        i = cp_i;
        words.push_back({text.substr(start, i - start), start, i});
    }
    return words;
}

static float sigmoid(float x) { return 1.0f / (1.0f + std::expf(-x)); }

static char *strdup_safe(const std::string &s) {
    char *p = (char *)malloc(s.size() + 1);
    memcpy(p, s.c_str(), s.size() + 1);
    return p;
}

// ─── C API ───

extern "C" {

const char *gliner_version(void) { return "0.2.0"; }

GlinerHandle gliner_load(const char *model_dir) {
    const OrtApi *api = OrtGetApiBase()->GetApi(ORT_API_VERSION);
    auto *m = new GlinerModel_();
    m->model_dir = model_dir;

    // Load config
    std::string config_path = std::string(model_dir) + "/gliner_config.json";
    std::ifstream cf(config_path);
    if (cf.is_open()) {
        // Minimal JSON parsing for max_width, ent_token, sep_token
        std::string content((std::istreambuf_iterator<char>(cf)), {});
        auto find_int = [&](const std::string &key, int def) -> int {
            auto pos = content.find("\"" + key + "\"");
            if (pos == std::string::npos) return def;
            pos = content.find(":", pos);
            return std::atoi(content.c_str() + pos + 1);
        };
        m->max_width = find_int("max_width", 12);
    }

    // Create ONNX Runtime session
    api->CreateEnv(ORT_LOGGING_LEVEL_WARNING, "gliner", &m->env);
    api->CreateSessionOptions(&m->opts);
    api->SetSessionGraphOptimizationLevel(m->opts, ORT_ENABLE_ALL);

    std::string onnx_path = std::string(model_dir) + "/model.onnx";
    OrtStatus *status = api->CreateSession(m->env, onnx_path.c_str(), m->opts, &m->session);
    if (status) {
        delete m;
        return nullptr;
    }

    // Load tokenizer
    std::string tok_path = std::string(model_dir) + "/tokenizer.json";
    m->tokenizer = hf_tokenizer_load(tok_path.c_str());

    return m;
}

void gliner_free(GlinerHandle handle) {
    delete handle;
}

GlinerResult gliner_predict(GlinerHandle handle,
                            const char *text,
                            const char **labels, int32_t num_labels,
                            float threshold) {
    GlinerResult result = {};
    if (!handle || !handle->session) {
        result.error_code = 1;
        result.error_msg = "Model not loaded";
        return result;
    }

    const OrtApi *api = OrtGetApiBase()->GetApi(ORT_API_VERSION);
    auto *m = handle;

    // Step 1: Split words
    auto words = split_words(text);
    int num_words = (int)words.size();
    if (num_words == 0) return result;

    // Step 2: Build prompt + text tokens
    std::vector<std::string> all_tokens;
    for (int i = 0; i < num_labels; i++) {
        all_tokens.push_back(m->ent_token);
        all_tokens.push_back(labels[i]);
    }
    all_tokens.push_back(m->sep_token);
    int prompt_len = (int)all_tokens.size();
    for (auto &w : words) all_tokens.push_back(w.text);

    // Step 3: Tokenize
    auto enc = hf_tokenize(m->tokenizer, all_tokens);
    int seq_len = (int)enc.input_ids.size();

    // Step 4: words_mask
    std::vector<int64_t> words_mask(seq_len, 0);
    std::vector<bool> seen(num_words + 1, false);
    for (int i = 0; i < seq_len; i++) {
        int wid = enc.word_ids[i];
        if (wid >= prompt_len) {
            int word_idx = wid - prompt_len + 1;  // 1-based
            if (!seen[word_idx]) {
                words_mask[i] = word_idx;
                seen[word_idx] = true;
            }
        }
    }

    // Step 5: text_lengths, span_idx, span_mask
    std::vector<int64_t> text_lengths = {(int64_t)num_words};
    int K = m->max_width;
    int num_spans = num_words * K;
    std::vector<int64_t> span_idx(num_spans * 2);
    std::vector<bool> span_mask_bool(num_spans);
    for (int s = 0; s < num_words; s++) {
        for (int k = 0; k < K; k++) {
            int idx = s * K + k;
            span_idx[idx * 2] = s;
            span_idx[idx * 2 + 1] = s + k;
            span_mask_bool[idx] = (s + k) < num_words;
        }
    }

    // Convert span_mask to uint8 for ONNX bool type
    std::vector<uint8_t> span_mask_u8(num_spans);
    for (int i = 0; i < num_spans; i++) span_mask_u8[i] = span_mask_bool[i] ? 1 : 0;

    // Step 6: Create ORT tensors and run
    OrtMemoryInfo *mem_info;
    api->CreateCpuMemoryInfo(OrtArenaAllocator, OrtMemTypeDefault, &mem_info);

    // Shapes
    int64_t ids_shape[] = {1, (int64_t)seq_len};
    int64_t tl_shape[] = {1, 1};
    int64_t sp_shape[] = {1, (int64_t)num_spans, 2};
    int64_t sm_shape[] = {1, (int64_t)num_spans};

    OrtValue *input_ids_t, *attn_t, *wm_t, *tl_t, *sp_t, *sm_t;
    api->CreateTensorWithDataAsOrtValue(mem_info, enc.input_ids.data(), seq_len * sizeof(int64_t), ids_shape, 2, ONNX_TENSOR_ELEMENT_DATA_TYPE_INT64, &input_ids_t);
    api->CreateTensorWithDataAsOrtValue(mem_info, enc.attention_mask.data(), seq_len * sizeof(int64_t), ids_shape, 2, ONNX_TENSOR_ELEMENT_DATA_TYPE_INT64, &attn_t);
    api->CreateTensorWithDataAsOrtValue(mem_info, words_mask.data(), seq_len * sizeof(int64_t), ids_shape, 2, ONNX_TENSOR_ELEMENT_DATA_TYPE_INT64, &wm_t);
    api->CreateTensorWithDataAsOrtValue(mem_info, text_lengths.data(), sizeof(int64_t), tl_shape, 2, ONNX_TENSOR_ELEMENT_DATA_TYPE_INT64, &tl_t);
    api->CreateTensorWithDataAsOrtValue(mem_info, span_idx.data(), num_spans * 2 * sizeof(int64_t), sp_shape, 3, ONNX_TENSOR_ELEMENT_DATA_TYPE_INT64, &sp_t);
    api->CreateTensorWithDataAsOrtValue(mem_info, span_mask_u8.data(), num_spans, sm_shape, 2, ONNX_TENSOR_ELEMENT_DATA_TYPE_BOOL, &sm_t);

    const char *input_names[] = {"input_ids", "attention_mask", "words_mask", "text_lengths", "span_idx", "span_mask"};
    const char *output_names[] = {"logits"};
    OrtValue *inputs[] = {input_ids_t, attn_t, wm_t, tl_t, sp_t, sm_t};
    OrtValue *output = nullptr;

    OrtStatus *run_status = api->Run(m->session, nullptr, input_names, (const OrtValue *const *)inputs, 6, output_names, 1, &output);

    if (run_status) {
        result.error_code = 2;
        result.error_msg = api->GetErrorMessage(run_status);
        goto cleanup;
    }
    if (!output) {
        result.error_code = 3;
        result.error_msg = "ONNX Run returned null output";
        goto cleanup;
    }

    {
        // Step 7: Decode logits
        float *logits_data = nullptr;
        OrtStatus *tstat = api->GetTensorMutableData(output, (void **)&logits_data);
        if (tstat) {
            result.error_code = 4;
            result.error_msg = api->GetErrorMessage(tstat);
            goto cleanup;
        }
        // If model output has 0 classes (e.g. labels not recognized), return empty
        if (!logits_data) goto cleanup;
        // Shape: (1, L, K, C) where L=num_words, K=max_width, C=num_labels
        int L = num_words, C = num_labels;

        struct Candidate { int start; int end; int cls; float score; };
        std::vector<Candidate> candidates;

        for (int s = 0; s < L; s++) {
            for (int k = 0; k < K; k++) {
                int end_word = s + k;
                if (end_word >= L) continue;
                for (int c = 0; c < C; c++) {
                    float logit = logits_data[((s * K) + k) * C + c];
                    float score = sigmoid(logit);
                    if (score > threshold) {
                        candidates.push_back({s, end_word, c, score});
                    }
                }
            }
        }

        // Sort by score descending
        std::sort(candidates.begin(), candidates.end(),
                  [](const Candidate &a, const Candidate &b) { return a.score > b.score; });

        // Greedy NMS
        std::vector<bool> occupied(L, false);
        std::vector<Candidate> selected;
        for (auto &cand : candidates) {
            bool overlap = false;
            for (int i = cand.start; i <= cand.end; i++) {
                if (occupied[i]) { overlap = true; break; }
            }
            if (overlap) continue;
            for (int i = cand.start; i <= cand.end; i++) occupied[i] = true;
            selected.push_back(cand);
        }

        // Build result
        result.num_entities = (int32_t)selected.size();
        if (result.num_entities > 0) {
            result.entities = (GlinerEntity *)calloc(result.num_entities, sizeof(GlinerEntity));
            for (int i = 0; i < result.num_entities; i++) {
                auto &sel = selected[i];
                // Use original text offsets for proper CJK entity text
                std::string ent_text = std::string(text).substr(
                    words[sel.start].start,
                    words[sel.end].end - words[sel.start].start);
                result.entities[i].text = strdup_safe(ent_text);
                result.entities[i].label = strdup_safe(labels[sel.cls]);
                result.entities[i].score = sel.score;
                result.entities[i].start = words[sel.start].start;
                result.entities[i].end = words[sel.end].end;
            }
        }
    }

cleanup:
    if (output) api->ReleaseValue(output);
    for (auto *v : inputs) api->ReleaseValue(v);
    api->ReleaseMemoryInfo(mem_info);
    return result;
}

void gliner_result_free(GlinerResult *result) {
    if (!result || !result->entities) return;
    for (int i = 0; i < result->num_entities; i++) {
        free((void *)result->entities[i].text);
        free((void *)result->entities[i].label);
    }
    free(result->entities);
    result->entities = nullptr;
    result->num_entities = 0;
}

} // extern "C"
