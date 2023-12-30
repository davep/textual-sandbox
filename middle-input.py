"""Example of a centred input."""

from textual.app import App, ComposeResult
from textual.containers import Container
from textual.widgets import Input

class MiddleInput(Container):

    DEFAULT_CSS = """
    MiddleInput {
        align: center middle;
        width: 90%;
        border: tall $background;
        height: 3;
        background: $surface;
    }

    MiddleInput:focus-within {
        border: tall $accent;
    }

    MiddleInput > Input {
        width: auto;
        max-width: 1fr;
        border: none;
        height: 1;
        background: $surface;
    }

    MiddleInput > Input:focus {
        border: none;
    }
    """

class MiddleInputApp(App[None]):

    CSS = """
    Screen {
        align: center middle;
    }
    """

    def compose(self) -> ComposeResult:
        yield MiddleInput(Input())
        yield MiddleInput(Input())
        yield MiddleInput(Input())
        yield MiddleInput(Input())
        yield MiddleInput(Input())

if __name__ == "__main__":
    MiddleInputApp().run()

### middle-input.py ends here
