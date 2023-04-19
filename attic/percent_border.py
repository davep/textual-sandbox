from textual.app        import App, ComposeResult
from textual.containers import Horizontal, Container
from textual.widgets    import Header, Footer, Label

class BorderPCentApp( App[ None ] ):

    CSS = """
    Container {
        height: 1fr;
        width: 1fr;
        background: $panel;
    }

    Container.old-border-type {
        border: outer red red inner red dashed red;
    }

    Container.new-border-type {
        /* TODO: Add support for a %age after the colour. */
        /* border: outer red 50%; */
        border: outer red;
    }
    """

    def compose( self ) -> ComposeResult:
        yield Header()
        yield Horizontal(
            Container( Label( "No border percentage" ), classes="old-border-type" ),
            Container( Label( "With border percentage" ), classes="new-border-type" ),
        )
        yield Footer()


if __name__ == "__main__":
    BorderPCentApp().run()
