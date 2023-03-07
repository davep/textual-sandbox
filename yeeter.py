from textual.app     import App, ComposeResult
from textual.binding import Binding
from textual.widgets import Header, Footer, ContentSwitcher, Label

class YeeterApp( App[ None ] ):

    CSS = """
    ContentSwitcher {
        align: center middle;
    }

    Label {
        border: solid red;
        background: red;
        color: yellow;
    }
    """

    BINDINGS = [
        Binding( f"{n}", f"yeet({n})", f"Child {n}" )
        for n in range( 10 )
    ]

    def compose( self ) -> ComposeResult:
        yield Header()
        with ContentSwitcher():
            for n in range( 10 ):
                yield Label( f"This is content #{n}", id=f"w{n}" )
        yield Footer()

    def action_yeet( self, choice ) -> None:
        self.query_one( ContentSwitcher ).current = f"w{choice}"

if __name__ == "__main__":
    YeeterApp().run()
