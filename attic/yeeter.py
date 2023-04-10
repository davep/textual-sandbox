from __future__ import annotations

from textual.app        import App, ComposeResult
from textual.containers import Vertical
from textual.binding    import Binding
from textual.widgets    import Header, Footer, ContentSwitcher, Label

class YeeterApp( App[ None ] ):

    CSS = """
    ContentSwitcher {
        align: center middle;
    }

    ContentSwitcher Label {
        border: solid red;
        background: red;
        color: yellow;
    }
    """

    BINDINGS = [ *[
        Binding( f"{n}", f"yeet({n})", f"Child {n}" )
        for n in range( 10 )
    ], Binding( "space", "yeet(None)", "None" )]

    def compose( self ) -> ComposeResult:
        yield Header()
        with Vertical():
            yield Label("Showing...",id="showing")
            with ContentSwitcher():
                for n in range( 10 ):
                    yield Label( f"This is content #{n}", id=f"w{n}" )
        yield Footer()

    def action_yeet( self, choice: int | None ) -> None:
        self.query_one( ContentSwitcher ).current = None if choice is None else f"w{choice}"
        self.query_one( "#showing", Label ).update( f"{self.query_one( ContentSwitcher ).visible_content!r}")

if __name__ == "__main__":
    YeeterApp().run()
