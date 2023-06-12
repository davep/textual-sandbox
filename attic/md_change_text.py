from textual.app     import App, ComposeResult
from textual.widgets import Header, Footer, Markdown

MD_TEXT = (
    """# This is example 1

Just some Markdown text.
""",
    """# This is example 2

This is a second bit of Markdown text
""",
    """# This is example 3

Yay! A third bit of text!
"""
)

class MDTextChangeApp( App[ None ] ):

    BINDINGS = [
        ( "1", "switch_to( 0 )", "MD 1" ),
        ( "2", "switch_to( 1 )", "MD 2" ),
        ( "3", "switch_to( 2 )", "MD 3" ),
    ]

    def compose( self ) -> ComposeResult:
        yield Header()
        yield Markdown( MD_TEXT[ 0 ] )
        yield Footer()

    async def action_switch_to( self, text: int ) -> None:
        await self.query_one( Markdown ).update( MD_TEXT[ text ] )

if __name__ == "__main__":
    MDTextChangeApp().run()
