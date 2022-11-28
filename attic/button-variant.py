"""https://github.com/Textualize/textual/issues/1188"""

from textual.app import App, ComposeResult
from textual.widgets import Button, Static

class ButtonApp( App[ None ] ):

    CSS = """
    Screen {
        align: center middle;
    }
    Static {
        width: auto;
    }
    """

    def compose(self) -> ComposeResult:
        yield Button( "This is a success button", variant="success" )
        yield Button( "This is a disabled success button", variant="success", disabled=True )
        yield Button( "This is a 'vanilla' button" )
        yield Button( "This is a invalid variant button", variant="launch" )
        yield Button( "This is a button with variant set to disabled", variant="disabled" )
        yield Static( id="css" )

    def on_button_pressed( self, event: Button.Pressed ) -> None:
        self.query_one( "#css", Static ).update( str( event.button.classes ) )

if __name__ == "__main__":
    ButtonApp().run()
