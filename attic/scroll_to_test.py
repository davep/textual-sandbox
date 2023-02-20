from textual.app        import App, ComposeResult
from textual.containers import Vertical
from textual.widgets    import Header, Footer, Button
from textual.binding    import Binding

class ScrollToTester( App[ None ] ):

    CSS = """
    Vertical {
        overflow-y: auto;
    }

    Button {
        margin: 1;
        width: 100%;
    }
    """

    BINDINGS = [
        Binding( "j", "jump", "Jump to a button off the screen" ),
    ]

    def compose( self ) -> ComposeResult:
        yield Header()
        yield Vertical(
            *[ Button( str( n ), id=f"btn-{n}" ) for n in range( 200 ) ]
        )
        yield Footer()

    def action_jump( self ) -> None:
        btn = self.query_one( "#btn-150", Button )
        self.query_one( Vertical ).scroll_to_widget( btn, force=True, animate=False )
        btn.focus()

if __name__ == "__main__":
    ScrollToTester().run()

### scroll_to_test.py ends here
