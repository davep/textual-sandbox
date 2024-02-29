"""Message tests for TabbedContent.

https://github.com/Textualize/textual/issues/3869
"""

from textual import on
from textual.app import App, ComposeResult
from textual.containers import Container, Horizontal
from textual.message import Message
from textual.widgets import Button, Log, TabbedContent, TabPane


class WrapperForTesting(Container):
    DEFAULT_CSS = """
    WrapperForTesting {
        Horizontal {
            height: auto;
        }
    }
    """

    def compose(self) -> ComposeResult:
        with Horizontal():
            yield Button("Select 3", id="select")
            yield Button("Clear", id="clear")
            yield Button("Hide all", id="hide-all")
        with TabbedContent():
            for title in ("One", "Two", "Three", "Four", "Five"):
                yield TabPane(title)

    @on(Button.Pressed, "#select")
    def select_tab(self) -> None:
        self.query_one(TabbedContent).active = "tab-3"

    @on(Button.Pressed, "#clear")
    def clear_tabs(self) -> None:
        self.query_one(TabbedContent).clear_panes()

    @on(Button.Pressed, "#hide-all")
    def hide_all(self) -> None:
        for n in range(5):
            self.query_one(TabbedContent).hide_tab(f"tab-{n+1}")


class TabbedContentMessagesTestingApp(App[None]):
    def compose(self) -> ComposeResult:
        yield WrapperForTesting()
        yield Log()

    @on(TabbedContent.TabActivated)
    @on(TabbedContent.Cleared)
    def log_message(self, event: Message):
        self.query_one(Log).write_line(f"{event!r}")


if __name__ == "__main__":
    TabbedContentMessagesTestingApp().run()

### tabbed_content_message_testing.py ends here
