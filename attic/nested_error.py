"""https://github.com/Textualize/textual/issues/3999"""

from textual.app import App, ComposeResult
from textual.widgets import Label


class NestedParseErrorApp(App[None]):
    CSS = """
    Screen {
        Label {
            border: solid red;
        }
        border: solid green;
    }
    """

    def compose(self) -> ComposeResult:
        yield Label("First", id="first")
        yield Label("Second", id="second")


if __name__ == "__main__":
    NestedParseErrorApp().run()

### nested_error.py ends here
