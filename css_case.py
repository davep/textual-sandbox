"""https://github.com/Textualize/textual/discussions/2298"""

from textual.app        import App, ComposeResult
from textual.containers import Vertical
from textual.widgets    import Header, Footer, Label

class ThisIsATest( Label ):
    pass

class ThisisaTest( Label ):
    pass

class Thisisatest( Label ):
    pass

class CSSCaseExampleApp( App[ None ] ):

    CSS = """
    ThisIsATest {
        border: round red;
    }

    ThisisaTest {
        border: round green;
    }

    Thisisatest {
        border: round blue;
    }
    """

    def compose( self ) -> ComposeResult:
        yield Header()
        with Vertical():
            yield ThisIsATest( "This is one class" )
            yield ThisisaTest( "This is another class" )
            yield Thisisatest( "And this is another still" )
        yield Footer()

if __name__ == "__main__":
    CSSCaseExampleApp().run()
