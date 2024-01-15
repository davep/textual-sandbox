"""Example of different types of selection."""

from textual.app import App, ComposeResult
from textual.containers import Vertical
from textual.widgets import Label

class SelectionTestApp(App[None]):

    def compose(self) -> ComposeResult:
        with Vertical(classes="user_message"):
            yield Label("This is the label", id="content_display")

    def on_mount(self) -> None:
        self.notify(
            f"{self.query_one('Vertical.user_message #content_display')}, "
            f"{self.query_one('.user_message #content_display')}"
        )

if __name__ == "__main__":
    SelectionTestApp().run()

### selection_test.py ends here
