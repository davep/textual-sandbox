from time import time

from textual.app import App, ComposeResult, RenderResult
from textual.widgets import Header, Label
from textual.widgets._header import HeaderClock

class UnixClock(HeaderClock):

    DEFAULT_CSS = """
    UnixClock {
        width: auto;
    }
    """

    def render(self) -> RenderResult:
        return str(time())

class OtherClockApp(App[None]):

    CSS = """
    Screen {
        align: center middle;
    }
    """

    def compose(self) -> ComposeResult:
        yield Header()
        yield Label("Here's a different kind of header clock")

    def on_mount(self) -> None:
        self.query_one(Header).mount(UnixClock())

if __name__ == "__main__":
    OtherClockApp().run()
