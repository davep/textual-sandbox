"""https://github.com/Textualize/textual/discussions/2551"""

from textual.app        import App, ComposeResult
from textual.containers import VerticalScroll
from textual.widgets    import Header, Footer, TabbedContent, TabPane, DataTable

class TwoTablesExampleApp( App[ None ] ):

    CSS = """
    TabbedContent ContentSwitcher {
        height: 1fr;
    }

    DataTable {
        height: 50%;
    }
    """

    def compose( self ) -> ComposeResult:
        yield Header()
        with TabbedContent():
            with TabPane( "Table 1" ):
                with VerticalScroll():
                    yield self.add_test_data( DataTable(), 10 )
            with TabPane( "Table 2" ):
                with VerticalScroll():
                    yield self.add_test_data( DataTable(), 100 )
        yield Footer()

    def add_test_data( self, table: DataTable, multiplier: int ) -> DataTable:
        table.add_columns( *[ f"Column {n}" for n in range( 5 ) ] )
        for _ in range( 200 ):
            table.add_row( *[ str( n * multiplier) for n in range( 5 ) ] )
        return table

if __name__ == "__main__":
    TwoTablesExampleApp().run()
