from typing import List
from collections import Counter

def unique_words_preserve_order(words: List[str]) -> List[str]:
    seen = set()
    result = []
    for word in words:
        if word not in seen:
            seen.add(word)
            result.append(word)
    return result


def top_k_frequent_first_tie(words: List[str], k: int) -> List[str]:
    if k <= 0:
        raise ValueError("k must be positive")
    
    counts = Counter(words)
    first_occurrence = {word: i for i, word in enumerate(words)}
    
    # sort by frequency (descending) then by first occurrence
    sorted_words = sorted(counts, key=lambda w: (-counts[w], first_occurrence[w]))
    
    return sorted_words[:k]


def redact_words(words: List[str], to_redact: List[str]) -> List[str]:
    redact_set = set(to_redact)
    return ["***" if word in redact_set else word for word in words]
