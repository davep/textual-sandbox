from textual.app         import App, ComposeResult, RenderResult
from textual.containers  import Vertical
from textual.widgets     import Header, Footer
from textual.scroll_view import ScrollView
from textual.geometry    import Size

class ScrollViewPlaceHolder( ScrollView ):

    def __init__( self, height: int ):
        super().__init__()
        self._height = height

    def on_mount( self ) -> None:
        self.virtual_size = Size( self.size.width, self._height )

    def render( self ) -> RenderResult:
        return "\n".join( (
            "".join( f"{n + 1:3}"[ 0 ] for n in range( self.size.width ) ),
            "".join( f"{n + 1:3}"[ 1 ] for n in range( self.size.width ) ),
            "".join( f"{n + 1:3}"[ 2 ] for n in range( self.size.width ) ),
            "", "",
            f"Size: {self.size!r}",
            f"Outer size: {self.outer_size!r}",
            f"Container size: {self.container_size!r}",
            f"Content region: {self.content_region!r}",
            f"Virtual size: {self.virtual_size!r}",
            f"Vertical scrollbar width: {self.scrollbar_size_vertical}",
            "",
            "Text to width:",
            "-" * self.size.width,
            "Text to width minus 2:",
            "-" * ( self.size.width - 2 ),
            "Text to width minus vertical scrollbar:",
            "-" * ( self.size.width - self.scrollbar_size_vertical ),
            "Text to width minus vertical scrollbar minus 2:",
            "-" * ( self.size.width - self.scrollbar_size_vertical - 2 ),
        ) )

class ScrollViewApp( App[ None ] ):

    CSS = """
    ScrollViewPlaceHolder {
        height: 1fr;
        border: round red;
    }
    """

    def compose( self ) -> ComposeResult:
        yield Header()
        yield Vertical( ScrollViewPlaceHolder( 1 ), ScrollViewPlaceHolder( 1000 ) )
        yield Footer()

if __name__ == "__main__":
    ScrollViewApp().run()
