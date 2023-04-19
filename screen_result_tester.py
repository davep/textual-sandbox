from __future__ import annotations

from textual.app        import App, ComposeResult
from textual.containers import Center, Horizontal
from textual.widgets    import Header, Footer, Button, Label
from textual.screen     import ModalScreen, Screen
from textual._context   import active_message_pump

class ScreenNoResult( Screen ):

    BINDINGS = [
        ( "space", "dismiss", "Close" ),
    ]

    def compose( self ) -> ComposeResult:
        yield Label( "This screen does nothing. Press SPACE to exit." )

class ScreenResult( Screen[ float ] ):

    BINDINGS = [
        ( "space", "result", "Close" ),
    ]

    def compose( self ) -> ComposeResult:
        yield Label( "This screen will return a value. Press SPACE to exit and see." )

    def action_result( self ) -> None:
        self.dismiss( 17.23 )

class ModalScreenNoResult( ModalScreen ):

    BINDINGS = [
        ( "space", "dismiss", "Close" ),
    ]

    def compose( self ) -> ComposeResult:
        yield Label( "This modal screen does nothing. Press SPACE to exit." )

class ModalScreenResult( ModalScreen[ int ] ):

    BINDINGS = [
        ( "space", "result", "Close" ),
    ]

    def compose( self ) -> ComposeResult:
        yield Label( "This modal screen will return a value. Press SPACE to exit and see." )

    def action_result( self ) -> None:
        self.dismiss( 42 )

class ResultFromBinding( ModalScreen[ str ] ):

    BINDINGS = [
        ( "space", "dismiss( 'This came from an action' )", "Close" ),
    ]

    def compose( self ) -> ComposeResult:
        yield Label( "This modal screen will return a value. Press SPACE to exit and see." )

class ScreenFromHell( ModalScreen[ bool ] ):

    BINDINGS = [
        ( "space", "dismiss( True )", "Close" ),
    ]

    def compose( self ) -> ComposeResult:
        yield Label( "This modal screen will return a value. Press SPACE to exit and see." )
        yield Button( "Let's go deeper with no callback!", id="no-callback" )
        yield Button( "Let's go deeper with a callback!", id="callback" )

    def on_button_pressed( self, event: Button.Pressed ) -> None:
        if event.button.id == "no-callback":
            self.app.push_screen( self )
        elif event.button.id == "callback":
            def foo( _: bool ) -> None:
                pass
            self.app.push_screen( ScreenFromHell(), foo )

class Main( Screen[ None ] ):

    DEFAULT_CSS = """
    Main > Horizontal {
        align: center middle;
        height: auto;
        width: 100%;
    }

    Button {
        margin-left: 3;
        margin-right: 3;
    }

    Label {
        margin-top: 3;
        padding: 1 4;
        background: $panel;
        width: auto;
        border: wide $primary;
    }
    """

    def compose( self ) -> ComposeResult:
        yield Header()
        with Horizontal():
            yield Button( "Screen, no result", id="screen_no_result" )
            yield Button( "Screen, result", id="screen_result" )
            yield Button( "Modal Screen, no result", id="modal_screen_no_result" )
            yield Button( "Modal Screen, result", id="modal_screen_result" )
            yield Button( "Screen, result from binding", id="screen_result_from_binding" )
            yield Button( "The Screen from [red]hell[/]", id="screen_from_hell" )
        with Center():
            yield Label( "Any result will appear here", id="res" )
        with Center():
            yield Label( "Message Result Here", id="msg")
        yield Footer()

    def on_button_pressed( self, event: Button.Pressed ) -> None:
        self.query_one( "#res", Label ).update( "No result" )
        self.query_one( "#msg", Label ).update( "No callback so no message pump")
        if event.button.id:
            getattr( self, event.button.id )()

    def screen_no_result( self ) -> None:
        self.app.push_screen( ScreenNoResult() )

    def screen_result( self ) -> None:
        async def handle_screen_result( result: float ) -> None:
            self.query_one( "#res", Label ).update( repr( result ) )
            self.query_one( "#msg", Label ).update( repr( active_message_pump.get() ) )
        self.app.push_screen( ScreenResult(), handle_screen_result )

    def modal_screen_no_result( self ) -> None:
        self.app.push_screen( ModalScreenNoResult() )

    def modal_screen_result( self ) -> None:
        def handle_screen_result( result: int ) -> None:
            self.query_one( "#res", Label ).update( repr( result ) )
            self.query_one( "#msg", Label ).update( repr( active_message_pump.get() ) )
        self.app.push_screen( ModalScreenResult(), handle_screen_result )

    def screen_result_from_binding( self ) -> None:
        def handle_screen_result( result: str ) -> None:
            self.query_one( "#res", Label ).update( repr( result ) )
            self.query_one( "#msg", Label ).update( repr( active_message_pump.get() ) )
        self.app.push_screen( ResultFromBinding(), handle_screen_result )

    def screen_from_hell( self ) -> None:
        async def handle_screen_result( result: bool ) -> None:
            self.query_one( "#res", Label ).update( repr( result ) )
            self.query_one( "#msg", Label ).update( repr( active_message_pump.get() ) )
        self.app.push_screen( ScreenFromHell(), handle_screen_result )

class ScreenResultTesterApp( App[ None ] ):

    CSS = """
    Screen {
        align: center middle;
    }
    """

    def on_mount( self ) -> None:
        self.push_screen(Main())

if __name__ == "__main__":
    ScreenResultTesterApp().run()
