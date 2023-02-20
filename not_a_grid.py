"""https://github.com/Textualize/textual/discussions/1844"""

from textual.app        import App, ComposeResult
from textual.containers import Horizontal, Vertical
from textual.widgets    import Header, Footer, TextLog, Input

class NotAGridLayout( App[ None ] ):

    CSS = """
    .left, .middle, .right {
        border: round #777;
    }

    .left, .right {
        width: 1fr;
    }

    .middle {
        width: 2fr;
    }

    TextLog {
        height: 1fr;
    }
    """

    def compose( self ) -> ComposeResult:
        yield Header()
        yield Vertical(
            Horizontal( TextLog( classes="left" ), TextLog( classes="middle" ), TextLog( classes="right" ) ),
            Horizontal(
                TextLog( classes="left" ),
                Vertical( TextLog(), Input( placeholder="Here's the Input" ), classes="middle" ),
                TextLog( classes="right" )
            ),
            Horizontal( TextLog( classes="left" ), TextLog( classes="middle" ), TextLog( classes="right" ) ),
        )
        yield Footer()

if __name__ == "__main__":
    NotAGridLayout().run()
