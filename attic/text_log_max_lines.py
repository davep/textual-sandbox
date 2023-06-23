"""https://github.com/Textualize/textual/discussions/2561"""

from textual.app        import App, ComposeResult
from textual.containers import Grid
from textual.widgets    import TextLog
from textual.reactive   import var

class TextLogMaxLinesApp( App[ None ] ):

    CSS = """
    Grid {
        grid-size: 3;
    }

    TextLog {
        border: solid yellow;
    }
    """

    line: var[ int ] = var( 0 )

    def compose( self ) -> ComposeResult:
        with Grid():
            for _ in range( 9 ):
                yield TextLog( max_lines=10 )

    def watch_line( self ) -> None:
        for log in self.query( TextLog ):
            log.write( str( self.line ) )

    def next_line( self ) -> None:
        self.line += 1

    def on_mount( self ) -> None:
        self.set_interval( 1 / 5, self.next_line )

if __name__ == "__main__":
    TextLogMaxLinesApp().run()
