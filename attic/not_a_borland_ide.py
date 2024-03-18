"""Quick and dirty Borland-a-like.

For a question on Discord.
"""

from pathlib import Path

from textual.app import App, ComposeResult
from textual.containers import Grid
from textual.widgets import Static, TextArea


class NotABorlandIDE(App[None]):
    CSS = """
    TextArea {
        height: 2fr;
        background: blue;
        border: double white;
    }

    #info {
        height: 1fr;
        keyline: heavy blue;
        grid-size: 3 1;
        grid-gutter: 1;
        background: cyan;
        Static {
            height: 1fr;
            color: blue;
        }
    }

    #footer {
        dock: bottom;
        height: 1;
        background: grey;
    }
    """

    def compose(self) -> ComposeResult:
        yield TextArea(Path(__file__).read_text(), language="python")
        with Grid(id="info"):
            yield Static("Here's some stuff")
            yield Static("More stuff here")
            yield Static("Oh look cool stuff!")
        yield Static("A bunch of cool stuff down here too!", id="footer")


if __name__ == "__main__":
    NotABorlandIDE().run()

### not_a_borland_ide.py ends here
