from textual.app        import App, ComposeResult
from textual.containers import Horizontal
from textual.widgets    import Header, Footer, Label, Switch

class LabeledSwitch( Horizontal ):

    def on_click( self ) -> None:
        self.query_one(Switch).toggle()

class ClickableLabelApp( App[ None ] ):

    def compose( self ) -> ComposeResult:
        yield Header()
        with LabeledSwitch():
            yield Label( "Click me!" )
            yield Switch()
        yield Footer()

if __name__ == "__main__":
    ClickableLabelApp().run()
