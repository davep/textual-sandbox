"""https://github.com/Textualize/textual/issues/1774"""

from textual.app        import App, ComposeResult
from textual.containers import Vertical
from textual.widgets    import Header, Footer, Static
from textual.binding    import Binding

class ScrollEndApp( App[ None ] ):

    BINDINGS = [
        Binding( str( n ), f"stuff( {n * 20} )", f"Stuff {n * 20}" ) for n in range( 1, 10 )
    ]

    def compose( self ) -> ComposeResult:
        yield Header()
        yield Vertical( Static( expand=True ) )
        yield Footer()

    def action_stuff( self, times: int ) -> None:
        self.query_one( Static ).update(
            "\n".join(
                f"This is test line #{n}" for n in range( times )
            )
        )
        self.query_one( Vertical ).scroll_end()

if __name__ == "__main__":
    ScrollEndApp().run()
