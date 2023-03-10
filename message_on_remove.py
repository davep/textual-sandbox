"""https://github.com/Textualize/textual/issues/2017"""

from textual.app        import App, ComposeResult
from textual.containers import Vertical
from textual.widgets    import Header, Footer, Button, TextLog
from textual.message    import Message

class MessageButton( Button ):

    DEFAULT_CSS = """
    MessageButton {
        width: 100%;
    }
    """

    class StuffHappened( Message ):

        def __init__( self, what: str ) -> None:
            super().__init__()
            self.what = what

    def on_mount( self ) -> None:
        self.post_message( self.StuffHappened( "I got added!" ) )

    def on_button_pressed( self ) -> None:
        self.post_message( self.StuffHappened( "I got removed!" ) )
        self.remove()


class MessasgeOnRemoveApp( App[ None ] ):

    CSS = """
    #buttons {
        border: round green;
        height: 2fr;
    }

    TextLog {
        border: round red;
        height: 1fr;
    }
    """

    BINDINGS = [
        ( "a", "add", "Add a button" ),
    ]

    def compose( self ) -> ComposeResult:
        yield Header()
        with Vertical():
            yield Vertical( id="buttons" )
            yield TextLog()
        yield Footer()

    def action_add( self ) -> None:
        self.query_one( "#buttons" ).mount( MessageButton( "Press me to remove me") )

    def on_message_button_stuff_happened( self, event: MessageButton.StuffHappened ):
        self.query_one( TextLog ).write( event.what )

if __name__ == "__main__":
    MessasgeOnRemoveApp().run()
