from textual.app        import App, ComposeResult
from textual.widgets    import Header, Footer, Button

class UnFancyButtonApp( App[ None ] ):

    CSS = """
    Screen {
        align: center middle;
    }

    Button {
        border: none;
        height: auto;
        width: auto;
        min-width: 0;
    }
    """

    def compose( self ) -> ComposeResult:
        yield Header()
        for n in range( 10 ):
            yield Button( f"Button {n}" )
        yield Footer()

if __name__ == "__main__":
    UnFancyButtonApp().run()
