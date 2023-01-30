from textual.app        import App, ComposeResult
from textual.containers import Vertical
from textual.widgets    import Header, Footer, Label, Input

class InputWidthAutoApp( App[ None ] ):

    CSS = """
    Input.fixed {
        width: 30;
    }
    Input.auto {
        width: auto;
    }
    Input.pcent {
        width: 20%;
    }
    """

    def compose( self ) -> ComposeResult:
        yield Header()
        yield Vertical(
            Label( "Default width:" ), Input( placeholder="This has default width" ),
            Label( "Fixed width:" ), Input( placeholder="This has a fixed width", classes="fixed" ),
            Label( "Auto width:" ), Input( placeholder="This has auto width", classes="auto" ),
            Label( "%age width:" ), Input( placeholder="This has %age width", classes="pcent" )
        )
        yield Footer()

if __name__ == "__main__":
    InputWidthAutoApp().run()
