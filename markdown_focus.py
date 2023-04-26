"""https://github.com/Textualize/textual/issues/2380"""

from textual.app        import App, ComposeResult
from textual.containers import VerticalScroll
from textual.widgets    import Header, Footer, Markdown

MARKDOWN = """\
# Header

## Sub Header

- List
- List
- List
- List
- List
- List

1. Another List
1. Another List
1. Another List
1. Another List
1. Another List
1. Another List
"""

class MarkdownFocusApp( App[ None ] ):

    CSS = """
    *:focus {
        border: double red;
    }
    """

    def compose( self ) -> ComposeResult:
        yield Header()
        with VerticalScroll():
            yield Markdown(MARKDOWN)
        yield Footer()

if __name__ == "__main__":
    MarkdownFocusApp().run()
