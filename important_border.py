"""https://github.com/Textualize/textual/issues/2420"""

from textual.app        import App, ComposeResult
from textual.containers import Grid
from textual.widgets    import Header, Footer, Static

class ImportantBorderApp( App[ None ] ):

    CSS = """
    Grid {
        grid-size: 3;
    }

    Static {
        content-align: center middle;
        border: round green !important;
        height: 1fr;
    }

    .subsequent {
        border: round red;
    }
    """

    def compose( self ) -> ComposeResult:
        yield Header()
        with Grid():
            for n in range( 9 ):
                yield Static(str(n), classes="subsequent")
        yield Footer()

if __name__ == "__main__":
    ImportantBorderApp().run()
