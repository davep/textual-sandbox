"""Code to test/demonstrate issue 1064.

https://github.com/Textualize/textual/issues/1064
"""

from sys import argv

from textual.app import App, ComposeResult
from textual.widgets import Static

class ArgApp( App[ None ] ):

    TITLE = "App that shows the command line arguments"

    def compose(self) -> ComposeResult:
        print( "I AM IN DEVTOOLS!" )
        yield Static( "\n".join( f"argv[ {n} ] = {v}" for n, v in enumerate( argv ) ) )

if __name__ == "__main__":
    ArgApp().run()

### issue_1060.py ends here
