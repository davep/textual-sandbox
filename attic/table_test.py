from textual.app import App, ComposeResult
from textual.containers import Vertical
from textual.widgets import Header, Footer, Static, DataTable

class MyDataTable( DataTable ):

    @property
    def cell_data( self ):
        return self.data[ self.cursor_cell.row ][ self.cursor_cell.column ]

    def watch_cursor_cell(self, old, value) -> None:
        self.app.query_one("#cell", Static).update( f"Current cell: {self.cell_data} ")
        return super().watch_cursor_cell(old, value)

class ProjectsList( Vertical ):

    DEFAULT_CSS = """
    MyDataTable {
        height: 1fr;
    }
    """

    def compose( self ) -> ComposeResult:
        yield Static( "Projects" )
        yield Static( id="cell" )
        yield MyDataTable()

    def on_mount( self ) -> None:
        table = self.query_one( MyDataTable )
        table.add_column( "Name" )
        for n in range( 30 ):
            table.add_row( f"Test {n}" )

class ProjectApp( App[ None ] ):

    def compose( self ) -> ComposeResult:
        yield Header()
        yield ProjectsList()
        yield Footer()

if __name__ == "__main__":
    ProjectApp().run()

