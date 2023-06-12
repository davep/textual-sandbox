from rich.text import Text

from textual.app        import App, ComposeResult
from textual.containers import Vertical, Horizontal
from textual.message    import Message
from textual.widgets    import Header, Footer, Checkbox, RadioButton, RadioSet, Button, TextLog, Label
from textual.css.query  import NoMatches

class ToggleTesterApp( App[ None ] ):

    BINDINGS = [ ( "d", "app.toggle_dark", "Toggle Dark Mode" ) ]

    CSS = """
    Vertical {
        border: round #666;
        height: 1fr;
        width: 1fr;
        background: $panel;
    }

    TextLog {
        border: round red;
        height: 3fr;
    }

    Horizontal > * {
        width: 1fr;
        height: 1fr;
    }

    RadioSet.grid {
        layout: grid;
        grid-size: 5 10;
    }

    #buttons {
        height: 3;
        align: center middle;
    }

    #buttons > Button {
        width: 100%;
    }

    #info {
        height: auto;
        background: $panel;
    }

    #info > Label {
        width: 1fr;
        height: 1;
        text-align: center;
    }
    """

    def compose( self ) -> ComposeResult:
        yield Header()
        yield RadioSet(":apple:"*50, ":car:"*50, ":pear:"*50)
        with Horizontal():
            with Vertical():
                yield Checkbox( "Checkbox 1\nLine 2\nLine 3" )
                yield Checkbox( Text.from_markup("Check[b][red]b[/][green]o[/][blue]x[/][/] 2"), button_first=False )
                yield Checkbox( "Checkbox 3" )
                yield Checkbox( "Checkbox 4", value=True )
            with RadioSet(id="rs1"):
                yield RadioButton("Radio Button 1", id="btn1", value=True)
                yield RadioButton("Radio Button 2", id="btn2", value=True)
                yield RadioButton("Radio Button 3", id="btn3", value=True)
                yield RadioButton("Radio Button 4", id="btn4", value=True)
            yield RadioSet( *[ f"[red]R[/][green]G[/][blue]B[/][i]{n}[/]" for n in range( 50 ) ], id="rs2", classes="grid" )
        with Horizontal( id="info" ):
            yield Label()
            yield Label(id="rs1")
            yield Label(id="rs2")
        with Horizontal( id="buttons" ):
            yield Button( "Toggle Disabled", id="disabled" )
        yield TextLog()
        yield Footer()

    async def _on_message( self, event: Message ) -> None:
        await super()._on_message( event )
        try:
            if isinstance( event, (
                    Checkbox.Changed, RadioButton.Changed, RadioSet.Changed
            ) ):
                self.query_one( TextLog ).write( f"For {event._handler_name} -- {repr( event )}" )
        except NoMatches:
            pass

    def on_button_pressed( self, event: Button.Pressed ) -> None:
        if event.button.id == "change":
            cb = self.query_one( "#changer", Checkbox )
            try:
                cb.label = str( int( str( cb.label ) ) + 1 )
            except ValueError:
                cb.label = "0"
        elif event.button.id == "disabled":
            self.query_one( ".grid", RadioSet ).disabled = not self.query_one( ".grid", RadioSet ).disabled

    def on_radio_set_changed( self, event: RadioSet.Changed ):
        if event.radio_set.id:
            self.query_one( f"Label#{event.radio_set.id}", Label ).update( f"Pressed: {event.radio_set.pressed_index}" )

if __name__ == "__main__":
    ToggleTesterApp().run()
