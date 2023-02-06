from textual.app        import App, ComposeResult
from textual.containers import Vertical
from textual.widgets    import Header, Footer, TextLog, DataTable

class TestDataTable( App[ None ] ):

    BINDINGS = (
        ("r", "row_mode", "Select Rows"),
    )

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
        yield Vertical( DataTable(), TextLog() )
        yield Footer()

    def on_mount(self) -> None:
        self.dt = self.query_one(DataTable)
        self.dt.add_columns('one', 'two')
        self.dt.add_rows([['1', '2'], ['a', 'b']])

    async def on_data_table_row_selected(self, row_selected: DataTable.RowSelected):
        self.query_one( TextLog ).write( row_selected )

    async def action_row_mode(self) -> None:
        self.dt.show_cursor = True
        self.dt.cursor_type = "row"

if __name__ == "__main__":
    TestDataTable().run()
