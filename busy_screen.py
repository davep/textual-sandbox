from time import sleep

from textual            import work
from textual.app        import App, ComposeResult
from textual.binding    import Binding
from textual.screen     import ModalScreen
from textual.widgets    import Header, Footer, Label, LoadingIndicator

class LoadingScreen( ModalScreen[ int ] ):

    def compose( self ) -> ComposeResult:
        """Compose the child widgets."""
        yield LoadingIndicator()

    def on_mount( self ) -> None:
        self.do_busy_work()

    @work
    def do_busy_work( self ) -> None:
        return_value = 0
        for n in range( 10 ):
            return_value += n
            sleep( 1 )
        self.app.call_from_thread( self.dismiss, return_value )

class BusyExampleApp( App[ None ] ):

    BINDINGS = [
        Binding( "space", "load", "Start the long load" ),
    ]

    def compose( self ) -> ComposeResult:
        yield Header()
        yield Label( "Press space to emulate loading" )
        yield Footer()

    def show_result( self, result: int ) -> None:
        self.query_one( Label ).update( f"The result was {result}" )

    def action_load( self ) -> None:
        self.push_screen( LoadingScreen(), callback=self.show_result )

if __name__ == "__main__":
    BusyExampleApp().run()
