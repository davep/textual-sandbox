from asyncio import run, sleep, Queue, create_task, wait_for, TimeoutError
from typing import AsyncIterator, AsyncIterable
from random import random

async def provider(prefix: str, count: int) -> AsyncIterator[str]:
    for n in range(count):
        await sleep(random())
        yield f"{prefix}-{n}"

async def consumer(source: AsyncIterable[str], queue: Queue[str]) -> None:
    async for next_item in source:
        await queue.put(next_item)

async def merge_providers(*providers: AsyncIterable[str]) -> AsyncIterator[str]:
    queue = Queue[str]()
    tasks = [create_task(consumer(provider, queue)) for provider in providers]
    while any(not task.done() for task in tasks):
        try:
            yield await wait_for(queue.get(), 0.1)
        except TimeoutError:
            pass
        else:
            queue.task_done()

async def main() -> None:
    async for hit in merge_providers(*[provider(str(n), 100) for n in range(10)]):
        print(hit)

run(main())
