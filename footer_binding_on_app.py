from textual.app      import App, ComposeResult
from textual.binding  import Binding
from textual.reactive import reactive
from textual.widgets  import Header, Footer, Label

class FooterBindingOnApp( App[ None ] ):

    BINDINGS = [
        Binding( "up", "up", "Press to get the highest score! (App)" ),
    ]

    score: reactive[int] = reactive(0)

    def compose( self ) -> ComposeResult:
        yield Header()
        yield Label()
        yield Footer()

    def action_up( self ) -> None:
        self.score += 1
        self.query_one( Label ).update( f"Score: {self.score}" )

if __name__ == "__main__":
    FooterBindingOnApp().run()
