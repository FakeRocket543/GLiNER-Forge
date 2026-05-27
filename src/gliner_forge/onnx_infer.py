"""Standalone GLiNER ONNX inference — no GLiNER library dependency.

Requires: onnxruntime, transformers (tokenizer only), numpy.
Works with models exported via GLiNER's save_pretrained() (single model.onnx).
"""
from __future__ import annotations
from pathlib import Path
from typing import Optional

import numpy as np
import onnxruntime as ort
from transformers import AutoTokenizer


class GLiNERStandalone:
    """Full GLiNER inference via ONNX Runtime.

    Replicates the library's UniEncoderSpan pipeline:
      prompt construction → tokenize → word mask → span generation → ONNX → decode
    """

    def __init__(self, model_dir: str | Path, providers: Optional[list[str]] = None):
        model_dir = Path(model_dir)
        onnx_path = model_dir / "model.onnx"
        if not onnx_path.exists():
            raise FileNotFoundError(f"No model.onnx in {model_dir}")

        if providers is None:
            providers = ["CoreMLExecutionProvider", "CPUExecutionProvider"]

        opts = ort.SessionOptions()
        opts.graph_optimization_level = ort.GraphOptimizationLevel.ORT_ENABLE_ALL
        self.session = ort.InferenceSession(str(onnx_path), opts, providers=providers)
        self.tokenizer = AutoTokenizer.from_pretrained(str(model_dir))

        # Read config
        import json
        config_path = model_dir / "gliner_config.json"
        cfg = json.loads(config_path.read_text()) if config_path.exists() else {}
        self.max_width = cfg.get("max_width", 12)
        self.ent_token = cfg.get("ent_token", "<<ENT>>")
        self.sep_token = cfg.get("sep_token", "<<SEP>>")
        self.words_splitter_type = cfg.get("words_splitter_type", "whitespace")

    def predict_entities(
        self, text: str, labels: list[str], threshold: float = 0.5, flat_ner: bool = True
    ) -> list[dict]:
        """Predict entities for a single text.

        Returns list of {"text", "label", "score", "start", "end"}.
        """
        # Step 1: Split text into words
        words, word_starts, word_ends = self._split_words(text)
        if not words:
            return []

        # Step 2: Build prompt tokens + text tokens
        prompt_tokens = []
        for label in labels:
            prompt_tokens.append(self.ent_token)
            prompt_tokens.append(label)
        prompt_tokens.append(self.sep_token)
        prompt_len = len(prompt_tokens)

        all_tokens = prompt_tokens + words

        # Step 3: Tokenize
        enc = self.tokenizer(
            all_tokens, is_split_into_words=True, return_tensors="np",
            padding=False, truncation=True, max_length=512
        )
        input_ids = enc["input_ids"].astype(np.int64)
        attention_mask = enc["attention_mask"].astype(np.int64)

        # Step 4: Build words_mask (map subword tokens → word indices, skipping prompt)
        words_mask = self._build_words_mask(enc, prompt_len)

        # Step 5: text_lengths
        num_words = len(words)
        text_lengths = np.array([[num_words]], dtype=np.int64)

        # Step 6: span_idx and span_mask
        span_idx, span_mask = self._build_spans(num_words)

        # Step 7: Run ONNX
        logits = self.session.run(None, {
            "input_ids": input_ids,
            "attention_mask": attention_mask,
            "words_mask": words_mask,
            "text_lengths": text_lengths,
            "span_idx": span_idx,
            "span_mask": span_mask,
        })[0]  # shape: (1, num_words, max_width, num_labels)

        # Step 8: Decode
        return self._decode(logits[0], words, labels, word_starts, word_ends, threshold, flat_ner, text)

    # CJK-aware: each CJK/Kana character is its own word; Hangul/alphabetic scripts use word boundaries
    _WORD_RE = __import__("re").compile(
        r"[\u4e00-\u9fff\u3400-\u4dbf\uf900-\ufaff]"  # CJK Unified Ideographs (char-level)
        r"|[\u3040-\u309f\u30a0-\u30ff]"                # Hiragana + Katakana (char-level)
        r"|[\uac00-\ud7af]+"                            # Hangul Syllables (word-level, space-separated)
        r"|[^\W\d_]+(?:[-_][^\W\d_]+)*"                 # Any alphabetic word (Latin, Cyrillic, Arabic, Thai, etc.)
        r"|[0-9]+(?:[.,][0-9]+)*"                       # Numbers
        r"|[^\s]"                                        # Other single non-space chars
    )

    def _split_words(self, text: str) -> tuple[list[str], list[int], list[int]]:
        """Split text into words. CJK: each character = 1 word. Others: standard tokenization."""
        words, starts, ends = [], [], []
        for m in self._WORD_RE.finditer(text):
            words.append(m.group())
            starts.append(m.start())
            ends.append(m.end())
        return words, starts, ends

    def _build_words_mask(self, enc, prompt_len: int) -> np.ndarray:
        """Build word-level mask: 0 for special/prompt tokens, 1-N for text words."""
        word_ids = enc.word_ids(0)
        mask = []
        for wid in word_ids:
            if wid is None or wid < prompt_len:
                mask.append(0)
            else:
                mask.append(wid - prompt_len + 1)
        # Deduplicate: only first subword of each word gets the mask value
        deduped = [0] * len(mask)
        seen = set()
        for i, v in enumerate(mask):
            if v > 0 and v not in seen:
                deduped[i] = v
                seen.add(v)
        return np.array([deduped], dtype=np.int64)

    def _build_spans(self, num_words: int) -> tuple[np.ndarray, np.ndarray]:
        """Generate all (start, end) span indices with width < max_width."""
        K = self.max_width
        spans = []
        for s in range(num_words):
            for w in range(K):
                spans.append([s, s + w])
        span_idx = np.array([spans], dtype=np.int64)  # (1, num_words*K, 2)
        # Mask: valid if end < num_words
        mask = np.array([[s + w < num_words for s in range(num_words) for w in range(K)]], dtype=bool)
        return span_idx, mask

    def _decode(
        self, logits: np.ndarray, words: list[str], labels: list[str],
        word_starts: list[int], word_ends: list[int], threshold: float, flat_ner: bool,
        original_text: str = ""
    ) -> list[dict]:
        """Decode logits (L, K, C) → entity list."""
        probs = 1.0 / (1.0 + np.exp(-logits))  # sigmoid
        L, K, C = probs.shape

        # Find all spans above threshold
        candidates = []
        for s in range(L):
            for k in range(K):
                end_word = s + k
                if end_word >= len(words):
                    continue
                for c in range(C):
                    score = float(probs[s, k, c])
                    if score > threshold:
                        candidates.append((s, end_word, c, score))

        # Sort by score descending
        candidates.sort(key=lambda x: -x[3])

        # Greedy NMS (flat NER: no overlaps)
        selected = []
        if flat_ner:
            occupied = set()
            for start, end, cls_idx, score in candidates:
                span_positions = set(range(start, end + 1))
                if span_positions & occupied:
                    continue
                occupied |= span_positions
                selected.append((start, end, cls_idx, score))
        else:
            selected = candidates

        # Convert to output format
        entities = []
        for start, end, cls_idx, score in selected:
            if cls_idx >= len(labels):
                continue
            entity_text = original_text[word_starts[start]:word_ends[end]]
            entities.append({
                "text": entity_text,
                "label": labels[cls_idx],
                "score": round(score, 4),
                "start": word_starts[start],
                "end": word_ends[end],
            })

        entities.sort(key=lambda x: x["start"])
        return entities


if __name__ == "__main__":
    import sys
    model_dir = sys.argv[1] if len(sys.argv) > 1 else str(Path(__file__).parent.parent.parent / "models" / "small-v2.5")
    m = GLiNERStandalone(model_dir)
    results = m.predict_entities(
        "Tim Cook is the CEO of Apple in Cupertino, California.",
        labels=["person", "organization", "location"],
        threshold=0.3,
    )
    for r in results:
        print(f"  {r['text']:20s} → {r['label']:15s} ({r['score']:.3f})")


def main():
    """CLI entry point."""
    import sys
    model_dir = sys.argv[1] if len(sys.argv) > 1 else str(Path(__file__).parent.parent.parent / "models" / "small-v2.5")
    text = sys.argv[2] if len(sys.argv) > 2 else "Tim Cook is the CEO of Apple in Cupertino, California."
    labels = sys.argv[3].split(",") if len(sys.argv) > 3 else ["person", "organization", "location"]
    m = GLiNERStandalone(model_dir)
    for r in m.predict_entities(text, labels, threshold=0.3):
        print(f"  {r['text']:20s} → {r['label']:15s} ({r['score']:.3f})")
