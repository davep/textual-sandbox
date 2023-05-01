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
        height: 1fr;
    }

    Static.border {
        border: round green !important;
    }

    Static.outline {
        outline: round green !important;
    }

    Static.both {
        border: round green !important;
        outline: round green !important;
    }

    Static.border.subsequent {
        border: round red;
    }

    Static.outline.subsequent {
        outline: round red;
    }

    Static.both.subsequent {
        border: round red;
        outline: round red;
    }
    """

    def compose( self ) -> ComposeResult:
        yield Header()
        options = ["outline", "border", "both"]
        with Grid():
            for n in range( 9 ):
                yield Static(
                    options[ n % 3 ],
                    classes=f"{options[ n % 3 ]} subsequent"
                )
        yield Footer()

if __name__ == "__main__":
    ImportantBorderApp().run()
