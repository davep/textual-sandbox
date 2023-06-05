"""https://github.com/Textualize/textual/discussions/2731"""

from textual.app import App, ComposeResult
from textual.containers import Vertical, Grid
from textual.widgets import Static


class Row(Grid):

    DEFAULT_CSS = """
    Row {
        layout: grid;
        grid-size: 2;
    }
    """

    def compose(self) -> ComposeResult:
        yield Static("Column 1")
        yield Static("Column 2")

class Demo(App):

    def compose(self) -> ComposeResult:
        with Vertical():
            for i in range(9):
                yield Row()

if __name__ == "__main__":
    Demo().run()
