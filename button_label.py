from textual.app import App, ComposeResult
from textual.widgets import Button

class ButtonApp( App[ None ] ):

    CSS = """
    Screen {
        align: center middle;
    }
    """

    def compose(self) -> ComposeResult:
        yield Button( "0", id="counter")

    def on_button_pressed( self, event: Button.Pressed ):
        if event.button.id == "counter":
            event.button.label = str( int( str( event.button.label ) ) + 1 )

if __name__ == "__main__":
    ButtonApp().run()

