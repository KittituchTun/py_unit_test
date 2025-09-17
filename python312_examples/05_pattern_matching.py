from __future__ import annotations


def describe_shape(shape: object) -> str:
    match shape:
        case {"type": "circle", "radius": r} if r > 0:
            return f"Circle with radius {r}"
        case {"type": "rectangle", "width": w, "height": h}:
            return f"Rectangle {w}x{h}"
        case [x, y]:
            return f"Point at ({x}, {y})"
        case _:
            return "Unknown shape"


def main() -> None:
    print(describe_shape({"type": "circle", "radius": 5}))
    print(describe_shape({"type": "rectangle", "width": 3, "height": 4}))
    print(describe_shape([10, 20]))
    print(describe_shape(None))


if __name__ == "__main__":
    main()

