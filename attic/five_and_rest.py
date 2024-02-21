from textual.app import App, ComposeResult
from textual.containers import Horizontal, Vertical
from textual.widgets import Header, Footer


class FiveAndRestApp(App[None]):

    CSS = """
    Vertical {
        border: round red;
    }

    #left {
        width: 5;
    }

    #right {
        width: 1fr;
    }
    """

    def compose(self) -> ComposeResult:
        yield Header()
        yield Horizontal(Vertical(id="left"), Vertical(id="right"))
        yield Footer()


if __name__ == "__main__":
    FiveAndRestApp().run()
