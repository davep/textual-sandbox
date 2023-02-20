from textual.app        import App, ComposeResult
from textual.containers import Vertical
from textual.widgets    import Header, Footer, Label, Input

class SetTitleApp( App[ None ] ):

    CSS = """
    Label {
        margin-left: 1;
    }

    Vertical {
        align: center middle;
    }
    """

    def compose( self ) -> ComposeResult:
        yield Header()
        yield Vertical(
            Label( "Set the terminal title:" ),
            Input( placeholder="Set the terminal title here" )
        )
        yield Footer()

    def on_input_changed( self, event: Input.Changed ) -> None:
        self.console.set_window_title( event.value )

if __name__ == "__main__":
    SetTitleApp().run()
