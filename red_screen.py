"""Example of setting the colour of the background of an app."""

from textual.app import App, ComposeResult
from textual.widgets import Label


class RedScreenApp(App[None]):
    CSS = """
    Screen {
        background: red;
    }
    """

    def compose(self) -> ComposeResult:
        yield Label("This is red")


if __name__ == "__main__":
    RedScreenApp().run()

### red_screen.py ends here
