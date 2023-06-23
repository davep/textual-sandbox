"""https://github.com/Textualize/textual/issues/2371"""

from textual.app        import App, ComposeResult
from textual.containers import Grid
from textual.widgets    import Header, Footer, Static

class OutlineApp( App[ None ] ):

    CSS = """
    Grid {
        grid-size: 3;
    }

    Static {
        content-align: center middle;
        height: 1fr;
    }

    Static.split {
        outline-top: thick green 30%;
        outline-left: thick green 30%;
        outline-bottom: thick green 30%;
        outline-right: thick green 30%;
    }

    Static.join {
        outline: thick green 30%;
    }
    """

    def compose( self ) -> ComposeResult:
        yield Header()
        with Grid():
            for n in range( 9 ):
                yield Static(
                    ( "outline-{parts}:" if n % 2 else "outline:" ), classes=( "split" if n % 2 else "join" )
                )
        yield Footer()

if __name__ == "__main__":
    OutlineApp().run()
