from textual.app        import App, ComposeResult
from textual.widgets    import Header, Footer, Input

class InputPopulate( App[ None ] ):

    CSS = """
    Screen {
        align: center middle;
    }
    """

    def compose( self ) -> ComposeResult:
        yield Header()
        yield Input( placeholder="Data will go here" )
        yield Footer()

    def on_mount( self ) -> None:
        self.query_one( Input ).value = "This is a test value"

if __name__ == "__main__":
    InputPopulate().run()
