"""https://github.com/Textualize/textual/discussions/2992"""

from textual.app import App, ComposeResult
from textual.containers import VerticalScroll, Horizontal
from textual.widgets import Static

class ScrollableGridApp(App[None]):

    CSS = """
    .row {
        height: 5;
    }

    .row Static {
        border: solid cornflowerblue;
        width: 1fr;
        height: 1fr;
    }
    """

    def compose(self) -> ComposeResult:
        with VerticalScroll():
            for y in range(20):
                with Horizontal(classes="row"):
                    for x in range(20):
                        yield Static(f"{y} {x}")

if __name__ == "__main__":
    ScrollableGridApp().run()
