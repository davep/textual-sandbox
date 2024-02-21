"""https://stackoverflow.com/questions/75714294/dynamically-determine-height-of-widget-in-python-textual"""

from textual.app import App, ComposeResult
from textual.containers import Vertical
from textual.widgets import Header, Footer, Static


class HeightApp(App[None]):

    CSS = """
    Static {
       border: round green;
    }

    #top {
        height: 20;
    }

    #bottom {
        height: 1fr;
    }
    """

    def compose(self) -> ComposeResult:
        yield Header()
        with Vertical():
            yield Static("This is 20 high", id="top")
            yield Static("This is the rest of the terminal high", id="bottom")
        yield Footer()


if __name__ == "__main__":
    HeightApp().run()
