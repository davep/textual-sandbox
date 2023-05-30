from textual            import on
from textual.app        import App, ComposeResult
from textual.containers import Center, Vertical
from textual.events     import ScreenResume, ScreenSuspend, Show
from textual.message    import Message
from textual.screen     import Screen
from textual.widgets    import Button, Label, TextLog

class TestScreen( Screen[ None ] ):

    DEFAULT_CSS = """
    Center {
        layout: horizontal;
    }

    Button {
        margin-left: 1;
        margin-right: 1;
    }

    TextLog {
        border: solid red;
    }

    TextLog:focus {
        border: double green;
    }
    """

    def __init__( self, depth: int=0 ) -> None:
        super().__init__()
        self._depth = depth

    def compose( self ) -> ComposeResult:
        """Compose the child widgets."""
        with Vertical():
            yield Label( f"Depth: {self._depth}")
            yield TextLog()
            with Center():
                yield Button( "Let's go deeper!", id="push" )
                yield Button( "Let's get out of here!", id="pop" )

    @on( Button.Pressed, "#push")
    def down( self ) -> None:
        self.app.push_screen( TestScreen( self._depth + 1 ) )

    @on( Button.Pressed, "#pop")
    def up( self ) -> None:
        self.dismiss( None )

    @on( ScreenResume )
    @on( ScreenSuspend )
    @on( Show )
    def message_log( self, event: Message ) -> None:
        self.query_one( TextLog ).write( f"{event!r}" )

class ScreenShowApp( App[ None ] ):

    def finish_up( self, _: None ) -> None:
        self.exit()

    def on_mount( self ) -> None:
        self.push_screen( TestScreen(), callback=self.finish_up )

if __name__ == "__main__":
    ScreenShowApp().run()
