"""https://github.com/Textualize/textual/discussions/2244"""

from textual.app import App, ComposeResult
from textual.containers import Vertical
from textual.widgets import Header, Footer, DataTable, Label


class CustomTable(Vertical):

    def __init__(self, title: str) -> None:
        super().__init__()
        self._title = title

    def _test_dt(self) -> DataTable:
        dt = DataTable()
        dt.zebra_stripes = True
        dt.cursor_type = "row"
        dt.fixed_columns = 1
        dt.add_column("id", width=10)
        dt.add_column("status", width=10)
        dt.add_column("description")
        for n in range(42):
            dt.add_row(n, f"Status {n}", f"This is description {n}")
        return dt

    def compose(self) -> ComposeResult:
        yield Label(self._title)
        yield self._test_dt()


class ThreeTablesApp(App[None]):

    CSS = """
    CustomTable {
        height: 1fr;
    }

    DataTable {
        height: 1fr;
    }
    """

    def compose(self) -> ComposeResult:
        yield Header()
        with Vertical():
            yield CustomTable("Table 1")
            yield CustomTable("Table 2")
            yield CustomTable("Table 3")
        yield Footer()


if __name__ == "__main__":
    ThreeTablesApp().run()
