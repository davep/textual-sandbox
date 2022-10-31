"""Code to test/demonstrate issue 1060.

https://github.com/Textualize/textual/issues/1060
"""

from textual.app import App, ComposeResult
from textual.widgets import Header, Static

class Demo( App[ None ] ):

    TITLE = "Demonstration"

    CSS = """
    Screen {
        layout: grid;
        grid-size: 2;
    }
    .box {
        height: 100%;
        border: white;
    }
    """

    def compose(self) -> ComposeResult:
        yield Header(show_clock=False)
        yield Static(classes="box")
        yield Static(classes="box")

if __name__ == "__main__":
    Demo().run()

### issue_1060.py ends here
