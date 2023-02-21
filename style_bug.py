"""https://github.com/Textualize/textual/issues/1852"""

from rich.text import Text

from textual.app        import App, ComposeResult, RenderResult
from textual.containers import Vertical
from textual.widgets    import Header, Footer
from textual.widget     import Widget

class Tester( Widget, can_focus=True ):

    COMPONENT_CLASSES = {
        "tester--text"
    }

    DEFAULT_CSS = """
    Tester {
        height: auto;
    }

    Tester:focus {
        display: block;
    }

    Tester:focus > .tester--text {
        background: red;
    }
    """

    def render( self ) -> RenderResult:
        return Text(
            "This is a test widget",
            style=self.get_component_rich_style( "tester--text" )
        )

class StyleBugApp( App[ None ] ):

    def compose( self ) -> ComposeResult:
        yield Header()
        yield Vertical( *[ Tester() for _ in range( 40 ) ] )
        yield Footer()

if __name__ == "__main__":
    StyleBugApp().run()
