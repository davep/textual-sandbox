"""https://github.com/Textualize/textual/discussions/1271"""

from textual.app import App, ComposeResult
from textual.widgets import Header, Footer
from textual.containers import Horizontal, Vertical
from textual.css.scalar import Scalar

class Splitter( App[ None ] ):

    CSS = """
    Horizontal {
        border: solid #666;
    }

    Vertical {
        border: solid #888;
        width: 1fr;
    }
    """

    BINDINGS = [
        ( "n", "new_pane", "New Pane" ),
        ( "w", "widen_first", "Widen First Pane" )
    ]

    def compose(self) -> ComposeResult:
        yield Header()
        yield Horizontal( id="main" )
        yield Footer()

    def action_new_pane( self ) -> None:
        self.query_one( "#main", Horizontal ).mount( Vertical() )

    def action_widen_first( self ) -> None:
        if len( panes := self.query( "#main Vertical" ) ) > 1:
            panes.first().styles.width = Scalar.parse( "2fr" )

if __name__ == "__main__":
    Splitter().run()

