from textual.app        import App, ComposeResult
from textual.containers import Container

class PastelBlackApp( App[ None ] ):

    CSS = """
    #top {
        border: black;
        background: grey;
    }

    #bottom {
        border: black;
        background: gray;
    }
    """

    def compose( self ) -> ComposeResult:
        yield Container( id="top" )
        yield Container( id="bottom" )

if __name__ == "__main__":
    PastelBlackApp().run()
