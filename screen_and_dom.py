from textual.app        import App, ComposeResult
from textual.containers import Vertical, Horizontal
from textual.widgets    import Header, Footer, Static, Label
from textual.screen     import Screen
from textual.binding    import Binding
from rich.pretty        import Pretty

class ChildScreen( Screen ):

    def compose( self ) -> ComposeResult:
        """Compose the child widgets."""
        yield Label( "Press space to make me go away", id="only-on-child" )

class Display( Static, can_focus=True ):
    pass

class DOMView( Display ):
    pass

class ScreenView( Display ):
    pass

class QueryResult( Display ):
    pass

class ScreenAndDomApp( App[ None ] ):

    CSS = """
    .box {
        border: round yellow;
    }
    .box:focus-within {
        border: double yellow;
    }

    Horizontal > Vertical {
        width: 1fr;
    }
    """

    BINDINGS = [
        Binding( "i", "install", "Install Screen" ),
        Binding( "u", "uninstall", "Uninstall Screen" )
    ]

    def __init__( self ) -> None:
        super().__init__()
        self.screen_id                 = 0
        self.screen_names: list[ str ] = []

    def compose( self ) -> ComposeResult:
        yield Header()
        yield Vertical(
            Vertical( DOMView(), classes="box" ),
            Horizontal(
                Vertical( ScreenView(), classes="box" ),
                Vertical( QueryResult(), classes="box" )
            )
        )
        yield Footer()

    @property
    def installed_screens( self ):
        return [ ( k, v ) for k, v in self._installed_screens.items() ]

    def refresh_panels( self ) -> None:
        self.query_one( DOMView ).update( self.tree )
        self.query_one( ScreenView ).update( Pretty( self.installed_screens ) )
        self.query_one( QueryResult ).update( Pretty( list( self.query( "#only-on-child" ) ) ) )

    def on_mount( self ) -> None:
        self.refresh_panels()

    def action_install( self ) -> None:
        self.screen_names.append( f"child-{ self.screen_id}" )
        self.screen_id += 1
        self.install_screen( ChildScreen(), self.screen_names[ -1 ] )
        self.refresh_panels()

    def action_uninstall( self ) -> None:
        if self.screen_names:
            self.uninstall_screen( self.screen_names.pop() )
            self.refresh_panels()

if __name__ == "__main__":
    ScreenAndDomApp().run()
