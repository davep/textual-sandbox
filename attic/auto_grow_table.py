"""https://github.com/Textualize/textual/issues/3160"""

from textual.app import App, ComposeResult
from textual.containers import Horizontal, Vertical
from textual.widgets import DataTable, Footer, Static


class ExpandingStatic(Static):

    def __init__(self) -> None:
        super().__init__()
        self._text = ""

    def add_row(self, row: str) -> None:
        self._text += f"{row}\n"
        self.update(self._text)


class AutoGrowTableApp(App[None]):

    CSS = """
    DataTable {
        border: panel red;
        height: auto;
    }

    ExpandingStatic {
        border: panel red;
        height: auto;
    }

    Vertical {
        border: panel cornflowerblue;
        height: auto;
    }
    """

    BINDINGS = [("space", "add_row", "Add another row to both tables")]

    def compose(self) -> ComposeResult:
        with Horizontal():
            yield DataTable()
            with Vertical() as v:
                v.border_title = "Vertical"
                yield DataTable()
            with Vertical() as v:
                v.border_title = "Vertical"
                yield ExpandingStatic()
        yield Footer()

    def on_mount(self) -> None:
        self.query_one(ExpandingStatic).border_title = "Static"
        for table in self.query(DataTable):
            table.border_title = "DataTable"
            table.add_columns("One", "Two", "Three")

    def action_add_row(self) -> None:
        self.query_one(ExpandingStatic).add_row("Another Static Line")
        for table in self.query(DataTable):
            table.add_row("Another", "Table", "Row!")


if __name__ == "__main__":
    AutoGrowTableApp().run()
