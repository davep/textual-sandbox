"""https://github.com/Textualize/textual/discussions/1844"""

from textual.app        import App, ComposeResult
from textual.containers import Horizontal, Vertical
from textual.widgets    import Header, Footer, TextLog, Input

class NotAGridLayout( App[ None ] ):

    CSS = """
    Horizontal > * {
        border: round #777;
    }

    Horizontal > Vertical {
        width: 2fr;
    }

    TextLog {
        height: 1fr;
        width: 1fr;
    }
    """

    def compose( self ) -> ComposeResult:
        yield Header()
        yield Vertical(
            Horizontal( TextLog(), TextLog(), TextLog() ),
            Horizontal(
                TextLog(),
                Vertical( TextLog(), Input( placeholder="Here's the Input" ) ),
                TextLog()
            ),
            Horizontal( TextLog(), TextLog(), TextLog() ),
        )
        yield Footer()

if __name__ == "__main__":
    NotAGridLayout().run()
