"""https://github.com/Textualize/textual/issues/2723"""

from textual.app     import App, ComposeResult
from textual.widgets import Static

class OneStatic( App[ None ] ):

    def compose( self ) -> ComposeResult:
        yield Static()

    def on_mount( self ) -> None:
        self.query_one( Static ).update( "Hello, World!" )

if __name__ == "__main__":
    OneStatic().run()
