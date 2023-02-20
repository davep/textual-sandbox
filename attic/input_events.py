from textual.app        import App, ComposeResult
from textual.containers import Vertical
from textual.widgets    import Header, Footer, Input, TextLog

class InputEventViewer( App[ None ] ):

    CSS = """
    TextLog {
        height: 1fr;
    }
    """

    def compose( self ) -> ComposeResult:
        yield Header()
        yield Vertical( Input(), TextLog() )
        yield Footer()

    def on_mount( self ) -> None:
        self.query_one( Input ).focus()

    def on_input_changed( self, event: Input.Changed ) -> None:
        self.query_one( TextLog ).write( ( event, event.input.value ) )

if __name__ == "__main__":
    InputEventViewer().run()
