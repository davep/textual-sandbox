"""https://github.com/Textualize/textual/issues/1481"""

from textual.app        import App, ComposeResult
from textual.containers import Vertical, Grid
from textual.widgets    import Header, Footer, Static
from textual.reactive   import reactive

class Box( Static ):

    DEFAULT_CSS = """
    Box {
        border: round green;
        width: 100%;
        height: 100%;
    }
    """

class DynaGrid( App[ None ] ):

    ROWS = 10

    grid_width = reactive( 10, init=False )

    BINDINGS = [
        ( "plus", "width(1)", "Increase" ),
        ( "minus", "width(-1)", "Decrease" )
    ]

    def compose( self ) -> ComposeResult:
        yield Header()
        yield Vertical()
        yield Footer()

    def on_mount( self ) -> None:
        body = self.query_one( Vertical )
        for _ in range( self.ROWS ):
            body.mount( row := Grid() )
            row.mount( *[ Box() for _ in range( self.grid_width ) ] )
            row.styles.grid_size_columns = self.grid_width

    async def watch_grid_width( self, new_val: int ) -> None:
        await self.query( Box ).remove()
        for row in self.query( Grid ):
            row.styles.grid_size_columns = self.grid_width
            await row.mount( *[ Box() for _ in range( self.grid_width ) ] )

    def action_width( self, by_val: int ) -> None:
        if self.grid_width > 1 or by_val > 0:
            self.grid_width += by_val

if __name__ == "__main__":
    DynaGrid().run()

### dynagrid.py ends here
