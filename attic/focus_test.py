"""https://github.com/Textualize/textual/issues/1879"""

from textual.app import App, ComposeResult
from textual.containers import Grid
from textual.widgets import Header, Footer, DataTable


class Focustest(App[None]):

    CSS = """
    Grid {
        grid-size: 4
    }

    DataTable .datatable--cursor {
        background: #333;
    }

    DataTable:focus .datatable--cursor {
        background: #c0c;
    }
    """

    @property
    def data_table(self) -> DataTable:
        data_table = DataTable[str]()
        data_table.add_columns("Column 1", "Column 2", "Column 3")
        data_table.add_rows([(str(n), str(n * 10), str(n * 100)) for n in range(10)])
        return data_table

    def compose(self) -> ComposeResult:
        yield Header()
        with Grid():
            for _ in range(16):
                yield self.data_table
        yield Footer()


if __name__ == "__main__":
    Focustest().run()
