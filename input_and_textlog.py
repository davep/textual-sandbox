from textual.app        import App, ComposeResult
from textual.containers import Vertical
from textual.widgets    import Header, Footer, Input, TextLog

class InputsAndTextLogApp( App[ None ] ):

    CSS = """
    #inputs {
        border: round red;
        height: auto;
    }

    TextLog {
        height: 1fr;
        border: round green;
    }
    """

    BINDINGS = [
        ( "l", "log", "Log some stuff" )
    ]

    def compose( self ) -> ComposeResult:
        yield Header()
        yield Vertical( *[
            Input( placeholder=f"Input {n}" )
            for n in range( 10 )
        ], id="inputs" )
        yield TextLog()
        yield Footer()

    def action_log( self ) -> None:
        log = self.query_one( TextLog )
        for n in range( 50 ):
            log.write( f"This is the really cool line {n}" )


if __name__ == "__main__":
    InputsAndTextLogApp().run()
