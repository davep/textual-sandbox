from asyncio import sleep
from dataclasses import dataclass

from textual import on, work
from textual.app import App, ComposeResult
from textual.containers import Vertical, Horizontal
from textual.message import Message
from textual.widgets import Label, Button

class AsyncWorkerExample(App[None]):

    CSS = """
    Vertical {
        border: solid grey;
    }
    """

    def compose(self) -> ComposeResult:
        with Horizontal():
            with Vertical():
                yield Button("Start inline update example", id="inline")
                yield Label("Waiting for you to hit the above button...", id="inline-result")
            with Vertical():
                yield Button("Start message-sending update example", id="messages")
                yield Label("Waiting for you to hit the above button...", id="message-result")

    ######################################################################
    # Doing it inline in the worker.

    @on(Button.Pressed, "#inline")
    def start_inline_worker(self) -> None:
        self.query_one("#inline-result", Label).update("Worker started...")
        self.run_inline()

    @work(exclusive=True, group="inline")
    async def run_inline(self) -> None:
        for n in range(500):
            await sleep(1)      # Fake working.
            self.query_one("#inline-result", Label).update(str(n))

    ######################################################################
    # Doing it via messages.

    @on(Button.Pressed, "#messages")
    def start_message_worker(self) -> None:
        self.query_one("#message-result", Label).update("Worker started...")
        self.run_using_messages()

    @dataclass
    class Counter(Message):
        count: int

    @work(exclusive=True, group="messages")
    async def run_using_messages(self) -> None:
        for n in range(500):
            await sleep(1)      # Fake working.
            self.post_message(self.Counter(n))

    @on(Counter)
    def update_message_counter(self, event: Counter) -> None:
        self.query_one("#message-result", Label).update(str(event.count))

if __name__ == "__main__":
    AsyncWorkerExample().run()
