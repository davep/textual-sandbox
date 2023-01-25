"""https://github.com/Textualize/textual/issues/1661"""

from textual.app     import App, ComposeResult
from textual.widgets import Header, Footer, TextLog
from textual.events  import Paste

class PasteEventLog( TextLog ):

    def on_paste( self, event: Paste ) -> None:
        self.write( repr( event.text ) )
        event.stop()

class PasteExplorer( App[ None ] ):

    def compose( self ) -> ComposeResult:
        yield Header()
        yield PasteEventLog()
        yield Footer()

    def on_mount( self ) -> None:
        self.query_one( PasteEventLog ).focus()

if __name__ == "__main__":
    PasteExplorer().run()

### paste_explorer.py ends here
