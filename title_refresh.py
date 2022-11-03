from textual.app import App, ComposeResult
from textual.widgets import Header
from textual.reactive import Reactive

class TitleApp( App[ None ] ):

    TITLE = "This is the TITLE"

    BINDINGS = [ ( "space", "title", "Next title" ) ]

    title_count = Reactive( 0 )

    def compose( self ) -> ComposeResult:
        yield Header()

    def watch_title_count( self, new_count: int ) -> None:
        self.title = f"{self.TITLE} - This is a refresh: {self.title_count}"

    def action_title( self ):
        self.title_count += 1

if __name__ == "__main__":
    TitleApp().run()

