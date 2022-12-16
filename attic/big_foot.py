from textual.app import App, ComposeResult
from textual.widgets import Static, Footer
from textual.binding import Binding

from rich.text import Text

class BigFooter( Footer ):

    def make_key_text(self) -> Text:
        text = super().make_key_text()
        text.overflow = "fold"
        text.no_wrap = False
        return text

class BigFoot( App[ None ] ):

    CSS = """
    BigFooter {
        height: auto;
    }
    """

    BINDINGS = [
        Binding(
            str( n ),
            f"bell( {n})",
            "This is some really long text about this"
        ) for n in range( 10 )
    ]

    def compose(self) -> ComposeResult:
        yield Static( "Stuff" )
        yield BigFooter()

if __name__ == "__main__":
    BigFoot().run()

