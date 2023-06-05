"""https://github.com/Textualize/textual/discussions/2731"""

from textual.app import App, ComposeResult
from textual.containers import Grid
from textual.widgets import Static


class Demo(App):
    CSS = """Grid {
        grid-size: 2;
    }
    """
    def compose(self) -> ComposeResult:
        with Grid():
            for i in range(9):
                yield Static("Column 1")
                yield Static("Column 2")

if __name__ == "__main__":
    Demo().run()
