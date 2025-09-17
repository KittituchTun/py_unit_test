from __future__ import annotations

import asyncio


async def fetch(value: int, delay: float) -> int:
    await asyncio.sleep(delay)
    return value * 2


async def run_tasks() -> list[int]:
    results: list[int] = []
    async with asyncio.TaskGroup() as tg:
        tasks = [
            tg.create_task(fetch(1, 0.2)),
            tg.create_task(fetch(2, 0.1)),
            tg.create_task(fetch(3, 0.3)),
        ]
    for task in tasks:
        results.append(task.result())
    return results


def main() -> None:
    results = asyncio.run(run_tasks())
    print("Async results:", results)


if __name__ == "__main__":
    main()

