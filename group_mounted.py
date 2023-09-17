"""https://github.com/Textualize/textual/discussions/3332"""

from dataclasses import dataclass

from textual import on
from textual.app import App, ComposeResult
from textual.containers import Horizontal, VerticalScroll
from textual.message import Message
from textual.widget import Widget
from textual.widgets import Button, Log

@dataclass
class CountMessage(Message):
    widget: Widget

class CheckingButton(Button):

    def on_mount(self) -> None:
        self.post_message(CountMessage(self))

class CollectionOfWidgets(VerticalScroll):

    DEFAULT_CSS = """
    CollectionOfWidgets Button {
        width: 1fr;
    }
    """

    def compose(self) -> ComposeResult:
        for n in range(100):
            yield CheckingButton(f"This is button {n}", id=f"button-{n}")

    def on_mount(self) -> None:
        self.post_message(CountMessage(self))

class KnowWhenOthersAreMountedApp(App[None]):

    def compose(self) -> ComposeResult:
        with Horizontal():
            yield CollectionOfWidgets()
            yield Log()

    @on(CountMessage)
    def log_count(self, event: CountMessage) -> None:
        self.query_one(Log).write_line(f"Mounted: {event.widget!r}")
        if len(event.widget.children):
            self.query_one(Log).write_line(f"    It also has {len(event.widget.children)} children")

if __name__ == "__main__":
    KnowWhenOthersAreMountedApp().run()

### group_mounted.py ends here
