"""https://github.com/Textualize/textual/issues/3615"""

import asyncio
from textual import work
from textual.app import App, ComposeResult
from textual.widgets import RichLog


class Test(App):
    CSS = """
    RichLog {
        height: 100%;
    }
    """

    def compose(self) -> ComposeResult:
        yield RichLog(id="log")

    def on_mount(self) -> None:
        self.my_worker()

    @work(exclusive=True, group="foo")
    async def my_worker(self):
        counter = 1

        log = self.query_one("#log", RichLog)
        while True:
            log.write(f"test {counter}")
            counter += 1
            await asyncio.sleep(1)


if __name__ == "__main__":
    Test().run()

### work_command.py ends here
