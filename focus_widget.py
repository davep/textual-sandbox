from textual.app        import App, ComposeResult, RenderResult
from textual.containers import Horizontal
from textual.widgets    import Header, Footer, Static
from textual.reactive   import reactive
from textual.binding    import Binding

class MyCoolWidget( Static, can_focus=True ):

    BINDINGS = [
        Binding( "m", "hello( 'Me' )", "Me" ),
        Binding( "w", "hello( 'World' )", "World" ),
    ]

    who = reactive( "World" )

    def render(self) -> RenderResult:
        return f"Hello, {self.who}!"

    def action_hello( self, who: str ) -> None:
        self.who = who

class FocusTestApp( App[ None ] ):

    CSS = """
    MyCoolWidget {
        width: 1fr;
        border: round red;
    }

    MyCoolWidget:focus {
        border: double yellow;
    }
    """

    def compose( self ) -> ComposeResult:
        yield Header()
        yield Horizontal(
            MyCoolWidget(),
            MyCoolWidget(),
            MyCoolWidget()
        )
        yield Footer()

    def on_mount( self ) -> None:
        # Focus the first one on startup.
        self.query( MyCoolWidget )[ 0 ].focus()

if __name__ == "__main__":
    FocusTestApp().run()
