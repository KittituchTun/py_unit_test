from __future__ import annotations

from pathlib import Path


def greet(name: str) -> str:
    return f"Hello, {name}!"


def show_paths() -> None:
    here = Path(__file__).resolve()
    project_root = here.parent
    print(f"This file: {here}")
    print(f"Project root: {project_root}")


def main() -> None:
    # Variables and f-strings
    user = "Python Learner"
    print(greet(user))

    # Pathlib basics
    show_paths()

    # Unpacking and comprehensions
    numbers = [1, 2, 3, 4, 5]
    squares = [n * n for n in numbers]
    print("Squares:", squares)

    first, *middle, last = numbers
    print("First:", first, "Middle:", middle, "Last:", last)


if __name__ == "__main__":
    main()

