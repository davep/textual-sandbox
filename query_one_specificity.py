"""Testing the specificity of query_one.

Mostly pondering the idea that querying for a Static will find a Button;
which I think makes sense, but which I also think might be confusing to some
folk. I feel that people may expect querying for a specific type to find
that specific type first.
"""

from textual.app        import App, ComposeResult
from textual.widgets    import Static, Button
from textual.containers import Vertical

class Specificity( App[ None ] ):

    CSS = """
    Screen { align: center middle; height: 50%; }
    Vertical { align: center middle; height: 50%; }
    Button { margin: 1; }
    Static { text-align: center; }
    """

    def compose( self ) -> ComposeResult:
        yield Vertical(
            Button( "query_one( Button )", id="button" ),
            Button( "query_one( Static )", id="static" ),
            Button( "query_one( 'Button' )", id="button_str" ),
            Button( "query_one( 'Static' )", id="static_str" )
        )
        yield Static( id="result" )

    def on_button_pressed( self, event: Button.Pressed ) -> None:
        find = dict(
            button=( Button, Button ),
            static=( Static, Static ),
            button_str=( "Button", Button ),
            static_str=( "Static", Static )
        )
        self.query_one( "#result", Static ).update(
            f"I found {self.query_one( *find[ event.button.id ] )}"
        )

if __name__ == "__main__":
    Specificity().run()
