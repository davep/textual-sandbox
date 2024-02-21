"""https://github.com/Textualize/textual/discussions/1943"""

from textual.app import App, ComposeResult
from textual.containers import Container, Horizontal
from textual.widgets import Header, Footer, Label, Static, Button, Switch


class Center(Horizontal):
    pass


class LeftFrame(Container):

    def compose(self) -> ComposeResult:
        yield Center(Label("Placeholder Text", id="question"))
        yield Center(Static("Calculate #"))
        yield Center(Button("Fullscreen", id="yes", variant="primary"))
        yield Center(Button("Draw!", id="no", variant="error"))
        yield Center(Switch())


class SazeyGitApp(App[None]):

    CSS = """
    Static {
        width: auto;
    }

    Center {
        align: center middle;
        height: auto;
    }
    """

    def compose(self) -> ComposeResult:
        yield Header()
        yield LeftFrame()
        yield Footer()


if __name__ == "__main__":
    SazeyGitApp().run()
