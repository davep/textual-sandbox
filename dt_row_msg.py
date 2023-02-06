from textual.app        import App, ComposeResult
from textual.containers import Vertical
from textual.widgets    import Header, Footer, TextLog, DataTable

class TestDataTable( App[ None ] ):

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
        yield Vertical( self.dt, TextLog() )
        yield Footer()

    def on_mount(self) -> None:
        self.dt.cursor_type = "row"
        self.dt.add_columns( "Row", *[ f"Column {n}" for n in range( 10 ) ] )
        for row in range( 50 ):
            self.dt.add_row( *[ str( row ), *[ str( n ) for n in range( 10 ) ] ] )
        self.dt.focus()

    async def on_data_table_row_selected(self, row_selected: DataTable.RowSelected):
        self.query_one( TextLog ).write( row_selected )

if __name__ == "__main__":
    TestDataTable().run()
