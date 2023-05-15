from textual.app        import App, ComposeResult
from textual.containers import Grid
from textual.widgets    import Header, Footer, DataTable

class ManyDataTablesApp( App[ None ] ):

    CSS = """
    Grid {
        grid-size: 4;
    }

    DataTable {
        border: solid yellow;
    }

    DataTable:focus {
        border: double yellow;
    }
    """

    def compose( self ) -> ComposeResult:
        yield Header()
        with Grid():
            for n in range( 32 ):
                yield self.configure( DataTable(), n )
        yield Footer()

    def configure( self, table: DataTable, number: int ) -> DataTable:
        table.border_title = str( number )
        table.add_columns( *[ str( n ) for n in range( 10 ) ] )
        for n in range( 100 ):
            table.add_row(
                *[ str( m * n ) for m in range( 10 ) ]
            )
        return table

if __name__ == "__main__":
    ManyDataTablesApp().run()
