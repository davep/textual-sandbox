from textual.app import App, ComposeResult
from textual.screen import Screen
from textual.widgets import Static, Header, Footer
from textual.binding import Binding
from textual.reactive import reactive

class BinaryScreen( Screen ):

    counter = reactive( 0, init=False )

    BINDINGS = [
        Binding( "h", "app.switch_screen( 'hex' )", "Switch to the hex counter" ),
        Binding( "up", "up", "Increase the counter" )
    ]

    def compose( self ) -> ComposeResult:
        yield Header()
        yield Static( "Press the up arrow to get counting" )
        yield Footer()

    def action_up( self ) -> None:
        self.counter += 1

    def watch_counter( self, new: int ) -> None:
        self.query_one( Static ).update( f"Your binary counter is now at {new:b}" )

class HexScreen( Screen ):

    counter = reactive( 0, init=True )

    BINDINGS = [
        Binding( "b", "app.switch_screen( 'binary' )", "Switch to the binary counter" ),
        Binding( "up", "up", "Increase the counter" )
    ]

    def compose( self ) -> ComposeResult:
        yield Header()
        yield Static( "Press the up arrow to get counting" )
        yield Footer()

    def action_up( self ) -> None:
        self.counter += 1

    def watch_counter( self, new: int ) -> None:
        self.query_one( Static ).update( f"Your hex counter is now at {new:x}" )

class ScreenSwapApp( App[ None ] ):

    CSS = """
    Screen {
        align: center middle;
    }
    Static {
        width: auto;
    }
    """

    SCREENS = {
        "binary": BinaryScreen,
        "hex": HexScreen
    }

    def on_mount( self ) -> None:
        self.push_screen( "binary" )

if __name__ == "__main__":
    ScreenSwapApp().run()
