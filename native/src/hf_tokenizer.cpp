/// hf_tokenizer.cpp — HuggingFace tokenizer via tokenizers-cpp (mlc-ai)
///
/// Implements pre-tokenized encoding with word_ids by encoding each word
/// individually and tracking which subword tokens belong to which word.
///
/// Requires: tokenizers-cpp (https://github.com/mlc-ai/tokenizers-cpp)
///   - libtokenizers_cpp.a + libtokenizers_c.a

#include <fstream>
#include <string>
#include <vector>

#include "tokenizers_cpp.h"

struct HFTokenizer {
    std::unique_ptr<tokenizers::Tokenizer> tok;
    int32_t cls_id = 101;   // [CLS]
    int32_t sep_id = 102;   // [SEP]
    int32_t pad_id = 0;     // [PAD]
};

struct TokenizeResult {
    std::vector<int64_t> input_ids;
    std::vector<int64_t> attention_mask;
    std::vector<int> word_ids;  // -1 for special tokens
};

static std::string read_file(const char *path) {
    std::ifstream f(path, std::ios::binary);
    return {std::istreambuf_iterator<char>(f), {}};
}

extern "C" {

HFTokenizer *hf_tokenizer_load(const char *tokenizer_json_path) {
    auto blob = read_file(tokenizer_json_path);
    if (blob.empty()) return nullptr;

    auto *t = new HFTokenizer();
    t->tok = tokenizers::Tokenizer::FromBlobJSON(blob);

    // Resolve special token IDs from vocab
    t->cls_id = t->tok->TokenToId("[CLS]");
    t->sep_id = t->tok->TokenToId("[SEP]");
    t->pad_id = t->tok->TokenToId("[PAD]");
    // Fallback for models using <s> / </s>
    if (t->cls_id < 0) t->cls_id = t->tok->TokenToId("<s>");
    if (t->sep_id < 0) t->sep_id = t->tok->TokenToId("</s>");
    if (t->pad_id < 0) t->pad_id = 0;

    return t;
}

void hf_tokenizer_free(HFTokenizer *tok) {
    delete tok;
}

} // extern "C"

TokenizeResult hf_tokenize(HFTokenizer *tok, const std::vector<std::string> &words) {
    TokenizeResult r;

    // [CLS]
    r.input_ids.push_back(tok->cls_id);
    r.attention_mask.push_back(1);
    r.word_ids.push_back(-1);

    // Encode each word separately → tracks word_ids
    for (int i = 0; i < (int)words.size(); i++) {
        auto ids = tok->tok->Encode(words[i]);
        // Skip special tokens that tokenizers-cpp may prepend/append
        // Most HF tokenizers add [CLS]=101 at start, [SEP]=102 at end when encoding
        // Strip them if present
        int start = 0, end = (int)ids.size();
        if (end > 0 && ids[0] == tok->cls_id) start++;
        if (end > start && ids[end - 1] == tok->sep_id) end--;

        for (int j = start; j < end; j++) {
            r.input_ids.push_back(ids[j]);
            r.attention_mask.push_back(1);
            r.word_ids.push_back(i);
        }
    }

    // [SEP]
    r.input_ids.push_back(tok->sep_id);
    r.attention_mask.push_back(1);
    r.word_ids.push_back(-1);

    return r;
}
