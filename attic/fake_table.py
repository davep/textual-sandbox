"""Example of using keyline to fake a table with Grid.

https://github.com/Textualize/textual/discussions/4186
"""

from textual.app import App, ComposeResult
from textual.containers import Grid
from textual.widgets import Label

DATA = (
    ("Released", "Title", "Box Office"),
    ("Dec 20, 2019", "Star Wars: The Rise of Skywalker", "$952,110,690"),
    ("May 25, 2018", "Solo: A Star Wars Story", "$393,151,347"),
    ("Dec 15, 2017", "Star Wars Ep. V111: The Last Jedi", "$1,332,539,889"),
    ("Dec 16, 2016", "Rogue One: A Star Wars Story", "$1,332,439,889"),
)


class FakeTableApp(App[None]):
    CSS = """
    Grid {
        grid-size: 3;
        grid-rows: 1;
        grid-columns: auto;
        grid-gutter: 1;
        keyline: thin;

        Label {
            width: 1fr;
            padding: 0 1 0 1;
        }
    }
    """

    def compose(self) -> ComposeResult:
        with Grid():
            for row in DATA:
                for col in row:
                    yield Label(col)


if __name__ == "__main__":
    FakeTableApp().run()

### fake_table.py ends here
