"""https://github.com/Textualize/textual/issues/2662"""

from textual.app        import App, ComposeResult
from textual.containers import Horizontal
from textual.widgets    import Select

class SelectBugApp( App[ None ] ):

    def on_mount( self ) -> None:
        self.query_one( Select ).value = 1

    def compose( self ) -> ComposeResult:
        yield Horizontal( Select( ( ( str( n ), n ) for n in range( 10 ) ) ) )

if __name__ == "__main__":
    SelectBugApp().run()
