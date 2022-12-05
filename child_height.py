from textual.app import App, ComposeResult
from textual.containers import Horizontal
from textual.widgets import Static, Header, Footer

class HeightApp( App[ None ] ):

    CSS = """
    Horizontal {
        border: solid red;
        height: auto;
    }

    Static {
        border: solid green;
        width: auto;
    }

    #fill_parent {
        height: 100%;
    }

    #static {
        height: 23;
    }
    """

    def compose( self ) -> ComposeResult:
        yield Header()
        yield Horizontal(
            Static( "How to make this as tall as container?", id="fill_parent" ),
            Static( "This has default\nheight\nbut a\nfew lines" ),
            Static( "I have a static height", id="static" ),
        )
        yield Footer()

if __name__ == "__main__":
    HeightApp().run()

