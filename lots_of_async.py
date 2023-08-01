from asyncio import run, sleep, Queue, create_task, wait_for, TimeoutError
from typing import AsyncIterator, AsyncIterable
from random import random

async def provider(prefix: str, count: int) -> AsyncIterator[str]:
    for n in range(count):
        yield f"{prefix}-{n}"
        await sleep(random() / 10)

async def consumer(source: AsyncIterable[str], queue: Queue[str]) -> None:
    async for next_item in source:
        await queue.put(next_item)

async def main():
    queue = Queue[str]()
    _ = [
        create_task(consumer(provider(str(n), 100), queue)) for n in range(10)
    ]
    gathered = 0
    while True:
        try:
            print(await wait_for(queue.get(), 0.1))
            gathered += 1
        except TimeoutError:
            break
        queue.task_done()

    print(f"Done! Gathered {gathered}")

run(main())
