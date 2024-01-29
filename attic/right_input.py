from textual.app import App, ComposeResult
from textual.widget import Widget
from textual.widgets import Input

class RightInput(Widget):

    DEFAULT_CSS = """
    RightInput {
        width: 1fr;
        height: auto;
        align-horizontal: right;
    }

    RightInput Input {
        width: auto;
    }
    """

    def compose(self) -> ComposeResult:
        yield Input()


class RightAlignInput(App[None]):

    def compose(self) -> ComposeResult:
        yield RightInput()
        yield RightInput()
        yield RightInput()
        yield RightInput()

if __name__ == "__main__":
    RightAlignInput().run()

### right_input.py ends here
