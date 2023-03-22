from textual.app     import App, ComposeResult
from textual.widgets import Header, Footer
from textual.binding import Binding

class MissingFooterStuffApp( App[ None ] ):

    BINDINGS = [
        Binding( "up", "oops(0)", "Up" ),
        Binding( "down", "oops(1)", "Down" ),
        Binding( "left", "oops(2)", "Left" ),
        Binding( "right", "oops(3)", "Right" ),
        Binding( "ctrl+up", "oops(4)", "Up" ),
        Binding( "ctrl+down", "oops(5)", "Down" ),
        Binding( "ctrl+left", "oops(6)", "Left" ),
        Binding( "ctrl+right", "oops(7)", "Right" ),
        Binding( "space", "oops(8)", "Space" ),
        Binding( "enter", "oops(9)", "Space" ),
        Binding( "q", "oops(10)", "Q" ),
    ]

    def compose( self ) -> ComposeResult:
        yield Header()
        yield Footer()

    def action_oops( self, _ ):
        self.app.exit()

if __name__ == "__main__":
    MissingFooterStuffApp().run()
