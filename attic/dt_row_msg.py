from textual.app import App, ComposeResult
from textual.containers import Vertical
from textual.widgets import Header, Footer, TextLog, DataTable
from textual.binding import Binding


class TestDataTable(App[None]):

    BINDINGS = [
        Binding("c", "cursor( 'cell' )", "Cell"),
        Binding("r", "cursor( 'row' )", "Row"),
        Binding("o", "cursor( 'column' )", "Column"),
    ]

    CSS = """
    DataTable {
        height: 1fr;
        border: round green;
    }

    DataTable:focus {
        border: double green;
    }

    TextLog {
        height: 1fr;
        border: round red;
    }

    TextLog:focus {
        border: double red;
    }
    """

    def compose(self) -> ComposeResult:
        yield Header()
        self.dt = DataTable()
        yield Vertical(self.dt, TextLog())
        yield Footer()

    def on_mount(self) -> None:
        self.dt.cursor_type = "row"
        self.dt.add_columns("Row", *[f"Column {n+1}" for n in range(10)])
        for row in range(50):
            self.dt.add_row(*[str(row), *[str(n) for n in range(10)]])
        self.dt.focus()

    def action_cursor(self, cursor: str) -> None:
        self.dt.cursor_type = cursor

    def on_data_table_cell_highlighted(self, event: DataTable.CellHighlighted) -> None:
        self.query_one(TextLog).write(event)

    def on_data_table_cell_selected(self, event: DataTable.CellSelected) -> None:
        self.query_one(TextLog).write(event)

    def on_data_table_row_selected(self, event: DataTable.RowSelected) -> None:
        self.query_one(TextLog).write(event)

    def on_data_table_row_highlighted(self, event: DataTable.RowHighlighted) -> None:
        self.query_one(TextLog).write(event)

    def on_data_table_column_selected(self, event: DataTable.ColumnSelected) -> None:
        self.query_one(TextLog).write(event)

    def on_data_table_column_highlighted(
        self, event: DataTable.ColumnHighlighted
    ) -> None:
        self.query_one(TextLog).write(event)


if __name__ == "__main__":
    TestDataTable().run()
