from dataclasses import dataclass

from textual            import on
from textual.app        import App, ComposeResult
from textual.containers import Horizontal, Vertical
from textual.message    import Message
from textual.widgets    import Header, Footer, TextLog, Button

class MessageFamily( Vertical ):

    DEFAULT_CSS = """
    MessageFamily {
        align: center middle;
    }

    MessageFamily Button {
        width: 90%;
        margin: 2;
    }
    """

    @dataclass
    class PressedParent( Message ):
        control: "MessageFamily"

    class PressedChild( PressedParent ):
        pass

    class PressedGrandchild( PressedChild ):
        pass

    class PressedGreatgrandchild( PressedGrandchild ):
        pass

    def compose( self ) -> ComposeResult:
        yield Button( "Press this to post the parent message", id="parent" )
        yield Button( "Press this to post the child message", id="child" )
        yield Button( "Press this to post the grandchild message", id="grandchild" )
        yield Button( "Press this to post the great-grandchild message", id="great-grandchild" )

    @on( Button.Pressed, "#parent" )
    def post_parent( self ) -> None:
        self.post_message( self.PressedParent( self ) )

    @on( Button.Pressed, "#child" )
    def post_child( self ) -> None:
        self.post_message( self.PressedChild( self ) )

    @on( Button.Pressed, "#grandchild" )
    def post_grandchild( self ) -> None:
        self.post_message( self.PressedGrandchild( self ) )

    @on( Button.Pressed, "#great-grandchild" )
    def post_greatgrandchild( self ) -> None:
        self.post_message( self.PressedGreatgrandchild( self ) )

class MessageSandboxApp( App[ None ] ):

    CSS = """
    TextLog {
        border: solid $primary-background;
        width: 2fr;
    }

    TextLog:focus {
        border: double $primary;
    }

    MessageFamily {
        border: solid $primary-background;
        width: 1fr;
    }

    MessageFamily:focus-within {
        border: double $primary;
    }
    """

    def compose( self ) -> ComposeResult:
        yield Header()
        with Horizontal():
            yield MessageFamily()
            yield TextLog()
        yield Footer()

    @on( MessageFamily.PressedParent )
    @on( MessageFamily.PressedChild )
    @on( MessageFamily.PressedGrandchild )
    @on( MessageFamily.PressedGreatgrandchild )
    def log_event( self, event: MessageFamily.PressedParent ) -> None:
        self.query_one( TextLog ).write( f"{event!r}" )

if __name__ == "__main__":
    MessageSandboxApp().run()
