from textual.app import App, ComposeResult
from textual.containers import Container, Vertical, Horizontal
from textual.widgets import Header, Footer


class MiyuLayoutApp(App[None]):

    CSS = """
    #left {
        width: 16;
    }

    #top-box {
        width: 1fr;
        height: 8;
        background: red;
    }

    #bottom-box {
        width: 1fr;
        height: 1fr;
        background: green;
    }

    #right {
        width: 1fr;
        height: 1fr;
        background: blue;
    }
    """

    def compose(self) -> ComposeResult:
        yield Header()
        with Horizontal():
            with Vertical(id="left"):
                yield Vertical(id="top-box")
                yield Container(id="bottom-box")
            yield Container(id="right")
        yield Footer()


if __name__ == "__main__":
    MiyuLayoutApp().run()
