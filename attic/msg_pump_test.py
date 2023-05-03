"""https://github.com/Textualize/textual/issues/2301"""

from textual.app        import App, ComposeResult
from textual.binding    import Binding
from textual.containers import Center
from textual.widgets    import Header, Footer, Button, Label
from textual._context   import active_message_pump

class MsgPumpApp( App[ None ] ):

    CSS = """
    Screen {
        align: center middle;
    }
    """

    BINDINGS = [
        Binding( "space", "show_pump", "Show Message Pump Within Action" ),
    ]

    def compose( self ) -> ComposeResult:
        yield Header()
        yield Center( Button( "Show Message Pump Within Message" ) )
        yield Center( Label( "Active Message Pump Will Be Reported Here" ) )
        yield Footer()

    def on_button_pressed( self ) -> None:
        self.query_one( Label ).update( f"{active_message_pump.get()!r}")

    def action_show_pump( self ) -> None:
        self.query_one( Label ).update( f"{active_message_pump.get()!r}")

if __name__ == "__main__":
    MsgPumpApp().run()
