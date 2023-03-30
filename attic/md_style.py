from inspect         import cleandoc
from textual.app     import App, ComposeResult
from textual.widgets import Header, Footer, Markdown

class MDStyleApp( App[ None ] ):

    CSS = """
    MarkdownH1 {
        text-align: left;
        width: auto;
        border: none;
        height: 1;
        padding: 0;
        background: red;
    }
    """

    def compose( self ) -> ComposeResult:
        yield Header()
        yield Markdown( cleandoc(
            """# This is a H1

            Here is some text.

            ## This is a H2

            Here is some more text.

            ### Here is a H3

            Here is even more text within the H3.
            """
        ) )
        yield Footer()

if __name__ == "__main__":
    MDStyleApp().run()
