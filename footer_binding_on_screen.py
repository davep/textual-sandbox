from textual.app      import App, ComposeResult
from textual.binding  import Binding
from textual.reactive import reactive
from textual.screen   import Screen
from textual.widgets  import Header, Footer, Label

class Game( Screen ):

    BINDINGS = [
        Binding( "up", "up", "Press to get the highest score! (Screen)" ),
    ]

    score: reactive[int] = reactive(0)

    def compose( self ) -> ComposeResult:
        yield Header()
        yield Label()
        yield Footer()

    def action_up( self ) -> None:
        self.score += 1
        self.query_one( Label ).update( f"Score: {self.score}" )

class FooterBindingOnScreen( App[ None ] ):

    def on_mount( self ) -> None:
        self.push_screen( Game() )

if __name__ == "__main__":
    FooterBindingOnScreen().run()
