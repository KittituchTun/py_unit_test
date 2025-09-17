from __future__ import annotations

from collections import Counter, defaultdict


def main() -> None:
    words = ["apple", "banana", "apple", "pear", "banana", "apple"]
    counts = Counter(words)
    print("Counts:", counts)

    # dict/set/list comprehensions
    lengths = {w: len(w) for w in words}
    uniques = {w for w in words}
    triples = [len(w) * 3 for w in words]
    print("Lengths:", lengths)
    print("Uniques:", uniques)
    print("Triples:", triples)

    # defaultdict
    groups: defaultdict[int, list[str]] = defaultdict(list)
    for word in words:
        groups[len(word)].append(word)
    print("Groups by length:", dict(groups))


if __name__ == "__main__":
    main()

