from __future__ import annotations

from typing import Iterable


def head[T](items: Iterable[T]) -> T | None:
    for item in items:
        return item
    return None


def pairify[T](a: T, b: T) -> tuple[T, T]:
    return (a, b)


def main() -> None:
    print("Head of [1,2,3]:", head([1, 2, 3]))
    print("Head of []:", head([]))
    print("Pairify:", pairify("x", "y"))


if __name__ == "__main__":
    main()

