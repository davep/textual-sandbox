from textual.app        import App, ComposeResult
from textual.containers import Container, Vertical
from textual.widgets    import Header, Footer, Placeholder

class LayoutSwitchApp( App[ None ] ):

    BINDINGS = [
        ( "t", "toggle", "Toggle Layout" ),
    ]

    CSS = """
    #main {
        layout: horizontal;
    }

    #left {
        width: 1fr;
        height: 1fr;
    }

    #left > Placeholder {
        height: 1fr;
    }

    #right {
        height: 1fr;
        width: 1fr;
    }

    #main.vertical {
        layout: vertical;
    }

    #main.vertical #left {
        height: 2fr;
    }
    """

    def compose( self ) -> ComposeResult:
        yield Header()
        yield Container(
            Vertical( Placeholder( "Top Left" ), Placeholder( "Bottom Left" ), id="left" ),
            Placeholder( "Right", id="right" ),
            id="main"
        )
        yield Footer()

    def action_toggle( self ) -> None:
        self.query_one( "#main", Container ).toggle_class( "vertical" )

if __name__ == "__main__":
    LayoutSwitchApp().run()
