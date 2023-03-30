from pathlib import Path

from textual.app     import App, ComposeResult
from textual.widgets import Header, Footer, MarkdownViewer
from textual.binding import Binding

class ViLikeMarkdownViewer( MarkdownViewer ):

    BINDINGS = [
        Binding( "j", "up", "", show=False ),
        Binding( "k", "down", "", show=False ),
    ]

    def action_up( self ) -> None:
        self.scroll_up()

    def action_down( self ) -> None:
        self.scroll_down()

class ViLikeMarkdownApp( App[ None ] ):

    def compose( self ) -> ComposeResult:
        yield Header()
        yield ViLikeMarkdownViewer( Path( "../textual/README.md" ).read_text() )
        yield Footer()

if __name__ == "__main__":
    ViLikeMarkdownApp().run()
