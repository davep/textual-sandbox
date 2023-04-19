from textual.app        import App, ComposeResult
from textual.containers import Vertical
from textual.widgets    import Header, Footer, Input, TextLog

class InputAndSomething( App[ None ] ):

    CSS = """
    TextLog {
        height: 1fr;
        border: round red;
    }
    """

    def compose( self ) -> ComposeResult:
        yield Header()
        with Vertical():
            yield Input( placeholder="Input a thing here" )
            yield TextLog()
        yield Footer()

    def on_input_submitted( self, event: Input.Submitted ) -> None:
        self.query_one( TextLog ).write( event.input.value )
        event.input.value = ""

    def on_mount( self ) -> None:
        self.query_one( Input ).focus()

if __name__ == "__main__":
    InputAndSomething().run()
