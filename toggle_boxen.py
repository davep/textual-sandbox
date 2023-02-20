from textual.app        import App, ComposeResult
from textual.containers import Vertical, Horizontal
from textual.message    import Message
from textual.widgets    import Header, Footer, Checkbox, RadioButton, RadioSet, Button, TextLog
from textual.css.query  import NoMatches

class ToggleTesterApp( App[ None ] ):

    CSS = """
    Vertical {
        border: round #666;
        height: 1fr;
        width: 1fr;
    }

    TextLog {
        border: round red;
        height: 3fr;
    }

    RadioSet {
        border: round #666;
        width: 1fr;
    }

    RadioSet.grid {
        layout: grid;
        grid-size: 5 10;
    }
    """

    def compose( self ) -> ComposeResult:
        yield Header()
        yield Horizontal(
            Vertical(
                Checkbox( "Checkbox 1" ),
                Checkbox( "Checkbox 2", button_first=False ),
                Checkbox( "Checkbox 3" ),
                Checkbox( "Checkbox 4", id="changer" ),
            ),
            RadioSet(
                RadioButton("Radio Button 1", id="btn1"),
                RadioButton("Radio Button 2", id="btn2"),
                RadioButton("Radio Button 3", id="btn3"),
                RadioButton("Radio Button 4", id="btn4"),
            ),
            RadioSet(
                *[ str( n ) for n in range( 50 ) ], classes="grid"
            ),
        )
        yield Button( "Change" )
        yield TextLog()
        yield Footer()

    async def _on_message( self, event: Message ) -> None:
        await super()._on_message( event )
        try:
            if isinstance( event, (
                    Checkbox.Changed, RadioButton.Changed, Checkbox.Selected, RadioButton.Selected,
                    RadioSet.Changed
            ) ):
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
