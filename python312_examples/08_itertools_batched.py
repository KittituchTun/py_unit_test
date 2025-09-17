from __future__ import annotations

from itertools import batched


def main() -> None:
    data = list(range(1, 11))
    for group in batched(data, 3):
        print("Batch:", list(group))


if __name__ == "__main__":
    main()

