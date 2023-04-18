"""https://github.com/Textualize/textual/discussions/2306"""

from random import randint

from textual.app        import App, ComposeResult
from textual.widgets    import Header, Footer, DataTable
from textual.coordinate import Coordinate

class CursorMoveApp( App[ None ] ):

    ROWS = 500

    def compose( self ) -> ComposeResult:
        yield Header()
        yield DataTable()
        yield Footer()

    def on_mount( self ) -> None:
        dt = self.query_one( DataTable )
        dt.focus()
        dt.add_columns( "Row", "Row * 10", "Row * 100", "Row * 1000" )
        dt.add_rows( [ (
            f"{n}",
            f"{n * 10}",
            f"{n * 100}",
            f"{n * 100}",
        ) for n in range( self.ROWS ) ] )
        self.set_interval( 0.5, self.move_cursor )

    def move_cursor( self ) -> None:
        self.query_one( DataTable ).cursor_coordinate = Coordinate(
            randint( 0, self.ROWS - 1 ),
            randint( 0, 3 )
        )

if __name__ == "__main__":
    CursorMoveApp().run()
