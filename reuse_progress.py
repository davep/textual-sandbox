"""https://github.com/Textualize/textual/issues/4096"""

from asyncio import sleep

from textual import on, work
from textual.app import App, ComposeResult
from textual.widgets import Button, ProgressBar


class ReuseProgressApp(App[None]):

    def compose(self) -> ComposeResult:
        yield Button("Count 10 seconds")
        yield ProgressBar()

    @on(Button.Pressed)
    def start_count(self) -> None:
        progress = self.query_one(ProgressBar)
        progress.total = 100
        progress.progress = 0
        self.count()

    @work
    async def count(self) -> None:
        for _ in range(100):
            self.query_one(ProgressBar).advance()
            await sleep(0.1)


if __name__ == "__main__":
    ReuseProgressApp().run()

### reuse_progress.py ends here
