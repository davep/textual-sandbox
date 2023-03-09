"""https://github.com/Textualize/textual/discussions/2009"""

from textual.app      import App, ComposeResult
from textual.widgets  import Header, Footer, Label
from textual.reactive import reactive

class MyLabel( Label ):

    DEFAULT_CSS = """
    .hidden {
        display: none;
    }
    """

    text: reactive[str | None] = reactive(None)

    def __init__( self ) -> None:
        super().__init__( classes="hidden" )

    def watch_text( self ) -> None:
        if self.text is not None:
            self.update( self.text )
        self.set_class( self.text is None, "hidden" )

class ReactShow( App[ None ] ):

    CSS = """
    Screen {
        align: center middle;
    }
    """

    BINDINGS = [
        ( "s", "set_text", "Set some text" ),
    ]

    def compose( self ) -> ComposeResult:
        yield Header()
        yield MyLabel()
        yield Footer()

    def action_set_text( self ) -> None:
        self.query_one( MyLabel ).text = "S U R P R I S E!!"

if __name__ == "__main__":
    ReactShow().run()
