"""https://github.com/Textualize/textual/discussions/2209"""

from textual.app        import App, ComposeResult
from textual.containers import Container
from textual.widgets    import Header, Footer

class BorderColourApp( App[ None ] ):

    CSS = """
    Screen {
        align: center middle;
    }
    Container {
        border: round red;
        width: 40%;
        height: 40%;
    }
    """

    def compose( self ) -> ComposeResult:
        yield Header()
        yield Container()
        yield Footer()

    def on_mount( self ):
        self.query_one( Container ).border_title = "[green]This isn't red![/]"
        self.query_one( Container ).border_subtitle = "[blue]Neither is this![/]"

if __name__ == "__main__":
    BorderColourApp().run()
