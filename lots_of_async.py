from asyncio import run, sleep, Queue, create_task, wait_for, TimeoutError
from typing import AsyncIterator, AsyncIterable, Callable
from random import random

async def provider(prefix: str, count: int) -> AsyncIterator[str]:
    for n in range(count):
        yield f"{prefix}-{n}"
        await sleep(random() / 10)

async def consumer(source: AsyncIterable[str], queue: Queue[str]) -> None:
    async for next_item in source:
        await queue.put(next_item)

async def merge_providers(*providers: AsyncIterable[str]) -> AsyncIterator[str]:
    queue = Queue[str]()
    _ = [create_task(consumer(provider, queue)) for provider in providers]
    while True:
        try:
            yield await wait_for(queue.get(), 0.1)
        except TimeoutError:
            break
        queue.task_done()

async def main() -> None:
    async for hit in merge_providers(*[provider(str(n), 100) for n in range(10)]):
        print(hit)

run(main())
