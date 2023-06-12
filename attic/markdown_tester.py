from textual.app     import App, ComposeResult
from textual.widgets import Header, Footer, Markdown

EXAMPLE = """
1. List 1
    1. SubList 1
    1. SubList 1
    1. SubList 1
    1. SubList 1
    1. SubList 1
1. List 2
1. List 3
1. List 4
1. List 5
1. List 6
1. List 7
1. List 8
1. List 9
1. List 10

"""

class MarkdownViewerApp( App[ None ] ):

    def compose( self ) -> ComposeResult:
        yield Header()
        yield Markdown( EXAMPLE )
        yield Footer()

if __name__ == "__main__":
    MarkdownViewerApp().run()
