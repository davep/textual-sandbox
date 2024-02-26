"""Testing from-code message posting.

https://github.com/Textualize/textual/issues/3869
"""

from textual import on
from textual.app import App, ComposeResult
from textual.message import Message
from textual.widgets import Button, Collapsible, Label, Log, TabbedContent, TabPane


class CollapsibleSandbox(TabPane):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__("Collapsible", *args, **kwargs)

    def compose(self) -> ComposeResult:
        yield Button("Toggle from code")
        with Collapsible():
            yield Label("Hello, World!")

    @on(Button.Pressed)
    def toggle_from_code(self) -> None:
        self.query_one(Collapsible).collapsed = not self.query_one(
            Collapsible
        ).collapsed


class MessageSandboxApp(App[None]):
    CSS = """
    TabbedContent {
        height: 1fr;
    }

    Log {
        height: 1fr;
        border-top: solid cornflowerblue;
    }
    """

    def compose(self) -> ComposeResult:
        with TabbedContent():
            yield CollapsibleSandbox()
        yield Log()

    @on(Collapsible.Toggled)
    def log_message(self, message: Message) -> None:
        self.query_one(Log).write_line(f"{message}")


if __name__ == "__main__":
    MessageSandboxApp().run()

### message_sandbox_redux.py ends here
