from string import ascii_lowercase

from textual.app        import App, ComposeResult
from textual.screen     import Screen
from textual.containers import Vertical, Horizontal
from textual.widgets    import Header, Footer, Label
from textual.binding    import Binding
from textual.events     import ScreenSuspend, ScreenResume

class Base( Screen ):

    def compose( self ) -> ComposeResult:
        """Compose the child widgets."""
        yield Header()
        yield Vertical(
            Horizontal( Label( f"This is [bold yellow]{self.__class__.__name__}[/]") ),
            Horizontal( Label( "[b]Press (almost) any key[/]" ) )
        )
        yield Footer()

    def on_screen_suspend( self, event: ScreenSuspend ) -> None:
        self.log( f"START SUSPEND IN {self.__class__.__name__}" )
        self.log( event )
        self.log( self.app.screen_stack )
        self.log( self.app.screen )
        self.log( f"END SUSPEND IN {self.__class__.__name__}" )

    def on_screen_resume( self, event: ScreenResume ) -> None:
        self.log( f"START RESUME IN {self.__class__.__name__}" )
        self.log( event )
        self.log( self.app.screen_stack )
        self.log( self.app.screen )
        self.log( f"END RESUME IN {self.__class__.__name__}" )

class This( Base ):

    BINDINGS = [
        Binding( key, f"any( '{key}' )", "This" ) for key in ascii_lowercase
    ]

    def action_any( self, _: str ) -> None:
        self.app.push_screen( "that" )

class That( Base ):

    BINDINGS = [
        Binding( key, f"any( '{key}' )", "That" ) for key in ascii_lowercase
    ]

    def action_any( self, _: str ) -> None:
        self.app.pop_screen()

class ScreenKeysApp( App[ None ] ):

    CSS = """
    Vertical {
        align: center middle;
        border: round red;
    }

    Horizontal {
        width: 100%;
        height: auto;
        align: center middle;
    }
    """

    SCREENS = {
        "this": This,
        "that": That
    }

    def on_mount( self ) -> None:
        self.push_screen( "this" )
        self.push_screen( "that" )

if __name__ == "__main__":
    ScreenKeysApp().run()

### screen_keys.py ends here
