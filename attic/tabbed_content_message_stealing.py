"""Example for https://github.com/Textualize/textual/issues/4233"""

from textual import on
from textual.app import App, ComposeResult
from textual.widgets import Button, TabbedContent, TabPane, Tabs


class TabbedContentMessageStealingApp(App[None]):
    CSS = """
    TabbedContent, TabPane {
        height: 1fr;
        width: 1fr;
    }
    """

    def compose(self) -> ComposeResult:
        with TabbedContent():
            with TabPane("Test", id="avoid-me"):
                yield Button("Disable", id="disable")
                yield Tabs("One", "Two", "Three", id="test-tabs")

    @on(Button.Pressed, "#disable")
    def disable_test(self) -> None:
        self.query_one("#test-tabs", Tabs).disable("tab-1")


if __name__ == "__main__":
    TabbedContentMessageStealingApp().run()

### tabbed_content_message_stealing.py ends here
