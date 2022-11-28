from textual.app import App, ComposeResult
from textual.widgets import Button

class MyButton( Button ):

    def __init__( self, caption, callback ):
        self.callback = callback
        super().__init__( caption )

    def press( self ):
        super().press()
        self.callback( self )

class ButtonApp( App[ None ] ):

    CSS = """
    Screen {
        align: center middle;
    }
    """

    def compose(self) -> ComposeResult:
        yield MyButton( "PUSH ME!", lambda btn: self.bell() )

if __name__ == "__main__":
    ButtonApp().run()

