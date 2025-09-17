from __future__ import annotations

import importlib
import sys
from pathlib import Path


EXAMPLES = [
    "01_basics",
    "02_collections",
    "03_functions",
    "04_classes_dataclasses",
    "05_pattern_matching",
    "06_typing_pep695",
    "07_asyncio",
    "08_itertools_batched",
]


def run_example(module_name: str) -> None:
    print(f"\n=== Running {module_name}.py ===")
    module = importlib.import_module(module_name)
    if hasattr(module, "main"):
        module.main()
    else:
        print("No main() found, importing executed module-level demo code.")


def main() -> None:
    sys.path.insert(0, str(Path(__file__).parent))
    for name in EXAMPLES:
        run_example(name)


if __name__ == "__main__":
    main()

