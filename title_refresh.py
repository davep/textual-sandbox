from textual.app import App, ComposeResult
from textual.widgets import Header

class TitleApp( App[ None ] ):

    TITLE = "This is the default title"

    BINDINGS = [ ( "space", "title", "Next title" ) ]

    title_count = 0

    def compose( self ) -> ComposeResult:
        yield Header()

    def action_title( self ):
        self.title_count += 1
        self.title = f"This is title iteration {self.title_count}"

if __name__ == "__main__":
    TitleApp().run()

