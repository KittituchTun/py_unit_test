from __future__ import annotations

from dataclasses import dataclass


class Vector2D:
    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y

    def __repr__(self) -> str:
        return f"Vector2D(x={self.x}, y={self.y})"

    def magnitude(self) -> float:
        return (self.x ** 2 + self.y ** 2) ** 0.5


@dataclass(order=True, frozen=True)
class Point:
    x: int
    y: int


def main() -> None:
    v = Vector2D(3.0, 4.0)
    print("Vector:", v, "| magnitude:", v.magnitude())

    p1 = Point(1, 2)
    p2 = Point(2, 1)
    print("Points sorted:", sorted([p2, p1]))
    # immutability enforced by frozen=True
    try:
        # type: ignore[attr-defined]
        p1.x = 10  # will raise FrozenInstanceError
    except Exception as exc:
        print("Attempt to mutate Point raised:", type(exc).__name__)


if __name__ == "__main__":
    main()

