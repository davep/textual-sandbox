"""https://github.com/Textualize/textual/issues/1999"""

from textual.app        import App, ComposeResult
from textual.containers import Vertical
from textual.widgets    import Header, Footer, Label, Button
from textual.screen     import Screen
from textual.binding    import Binding

class Child( Screen ):

    def compose( self ) -> ComposeResult:
        yield Header()
        with Vertical():
            yield Label( "This is the child screen" )
            yield Button( "Close Me" )
        yield Footer()

    def on_button_pressed( self, _: Button.Pressed ) -> None:
        self.app.pop_screen()

class Main( Screen ):

    def compose( self ) -> ComposeResult:
        yield Header()
        with Vertical():
            yield Label( "This is the main screen" )
            yield Button( "Show Child" )
        yield Footer()

    def on_button_pressed( self, _: Button.Pressed ) -> None:
        self.app.push_screen( Child() )

class DarkToggleTest( App[ None ] ):

    BINDINGS = [
        Binding( "d", "app.toggle_dark", "Toggle Light/Dark" ),
    ]


    CSS = """
    Vertical {
        align: center middle;
    }
    """

    def on_mount( self ) -> None:
        """"""
        self.push_screen( Main() )

if __name__ == "__main__":
    DarkToggleTest().run()
