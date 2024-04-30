"""Grid size test/example."""

from random import choice, randrange

from textual.app import App, ComposeResult
from textual.containers import Grid, Vertical
from textual.widgets import Button, Label


class Item(Vertical):
    DEFAULT_CSS = """
    Item {
        height: auto;
        background: $panel;
        Button, Label {
            width: 1fr;
        }
    }
    """

    def __init__(self, title: str, info: str, description: str) -> None:
        super().__init__()
        self._title = title
        self._info = info
        self._description = description

    def compose(self) -> ComposeResult:
        yield Label(self._title, id="title")
        yield Label(self._info, id="info")
        yield Label(self._description, id="description")
        yield Button("Button")


class GridLayoutExampleApp(App[None]):
    CSS = """
    Grid {
        grid-size: 3;
        grid-rows: auto;
        grid-gutter: 1 2;
        background: $background-lighten-2;
        width: 50;
    }
    """

    def compose(self) -> ComposeResult:
        with Grid():
            for n in range(5):
                yield Item(f"Small {n}", "Smol", "This is a smol one.")
                for m in range(2):
                    yield Item(
                        f"Bug {n}-{m}",
                        "Big",
                        choice(["Foo ", "Bar ", "Baz ", "Wibble ", "Wobble "])
                        * randrange(10, 30),
                    )


if __name__ == "__main__":
    GridLayoutExampleApp().run()

### grid_sizing.py ends here
