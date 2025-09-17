from __future__ import annotations


def add(a, b, /, *, scale: float = 1.0) -> float:
    # a, b are positional-only; scale is keyword-only
    return (a + b) * scale


def classify(value: object) -> str:
    match value:
        case int() as n if n % 2 == 0:
            return "even integer"
        case int():
            return "odd integer"
        case str() as s if s.isalpha():
            return "alphabetic string"
        case _:
            return "other"


def main() -> None:
    print("Add:", add(2, 3, scale=2))
    print("Classify 4:", classify(4))
    print("Classify 'abc':", classify("abc"))
    print("Classify 3.14:", classify(3.14))


if __name__ == "__main__":
    main()

