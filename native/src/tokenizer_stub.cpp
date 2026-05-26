/// tokenizer_stub.cpp — Stub HF tokenizer interface
/// Replace with tokenizers-cpp or sentencepiece+vocab implementation.
///
/// The real implementation needs:
///   1. Load tokenizer.json (HuggingFace fast tokenizer format)
///   2. Encode pre-split words with is_pretokenized=true
///   3. Return input_ids, attention_mask, and word_ids mapping

#include <string>
#include <vector>
#include <cstdio>

struct HFTokenizer {
    std::string path;
    // TODO: actual tokenizer state (BPE model, vocab, etc.)
};

struct TokenizeResult {
    std::vector<int64_t> input_ids;
    std::vector<int64_t> attention_mask;
    std::vector<int> word_ids;
};

extern "C" {

HFTokenizer *hf_tokenizer_load(const char *tokenizer_json_path) {
    auto *tok = new HFTokenizer();
    tok->path = tokenizer_json_path;
    fprintf(stderr, "[gliner] tokenizer stub loaded: %s\n", tokenizer_json_path);
    fprintf(stderr, "[gliner] WARNING: using stub tokenizer — inference will not produce correct results\n");
    fprintf(stderr, "[gliner] Link tokenizers-cpp or implement real tokenizer for production use\n");
    return tok;
}

void hf_tokenizer_free(HFTokenizer *tok) {
    delete tok;
}

} // extern "C"

TokenizeResult hf_tokenize(HFTokenizer * /*tok*/, const std::vector<std::string> &words) {
    // Stub: assign sequential IDs (WRONG but compiles)
    TokenizeResult r;
    r.input_ids.push_back(1);  // [CLS]
    r.attention_mask.push_back(1);
    r.word_ids.push_back(-1);
    for (int i = 0; i < (int)words.size(); i++) {
        r.input_ids.push_back(100 + i);  // fake token ID
        r.attention_mask.push_back(1);
        r.word_ids.push_back(i);
    }
    r.input_ids.push_back(2);  // [SEP]
    r.attention_mask.push_back(1);
    r.word_ids.push_back(-1);
    return r;
}
