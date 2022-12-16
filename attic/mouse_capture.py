from textual.app import App, ComposeResult
from textual.containers import Vertical
from textual.widgets import Static, TextLog
from textual.events import MouseMove, Key

class MouseArea( Static ):

    def on_mount( self ) -> None:
        self.capture_mouse()
        self.screen.query_one( TextLog ).write( "Mouse area mounted" )

    def on_mouse_move( self, event: MouseMove ) -> None:
        self.screen.query_one( TextLog ).write( f"Mouse move: {event!r}" )

class Report( TextLog ):
    pass

class MouseApp( App[ None ] ):

    CSS = """
    MouseArea {
        height: 1fr;
        background: #005500;
    }
    Report {
        height: 1fr;
        background: #888888;
        color: black;
    }
    """

    def compose( self ) -> ComposeResult:
        yield Vertical(
            MouseArea(),
            Report()
        )

    def on_key( self, event: Key ) -> None:
        if event.key.isdecimal():
            self.query_one( TextLog ).write( f"Key: {event!r}" )

if __name__ == "__main__":
    MouseApp().run()
