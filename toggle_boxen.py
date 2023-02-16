from textual.app        import App, ComposeResult
from textual.containers import Vertical
from textual.message    import Message
from textual.widgets    import Header, Footer, Checkbox, RadioButton, Button, TextLog
from textual.css.query  import NoMatches

class ToggleTesterApp( App[ None ] ):

    CSS = """
    Vertical {
        border: solid red;
        height: 1fr;
        width: 30%;
    }

    TextLog {
        border: round red;
        height: 3fr;
    }
    """

    def compose( self ) -> ComposeResult:
        yield Header()
        yield Vertical(
            Checkbox( "Checkbox 1" ),
            Checkbox( "Checkbox 2", button_first=False ),
            Checkbox( "Checkbox 3" ),
            Checkbox( "Checkbox 4", id="changer" ),
            RadioButton( "Radio Button 1" ),
            RadioButton( "Radio Button 2" ),
            RadioButton( "Radio Button 3" ),
            RadioButton( "Radio Button 4" ),
        )
        yield Button( "Change" )
        yield TextLog()
        yield Footer()

    async def _on_message( self, event: Message ) -> None:
        await super()._on_message( event )
        try:
            if isinstance( event, Checkbox.Changed ):
                self.query_one( TextLog ).write( f"For {event._handler_name} -- {repr( event )}" )
        except NoMatches:
            pass

    def on_button_pressed( self, _: Button.Pressed ) -> None:
        cb = self.query_one( "#changer", Checkbox )
        try:
            cb.label = str( int( str( cb.label ) ) + 1 )
        except ValueError:
            cb.label = "0"

if __name__ == "__main__":
    ToggleTesterApp().run()
