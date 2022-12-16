from textual.app import App, ComposeResult
from textual.widgets import Header, Static, Footer
from textual.containers import Container

class Issue1122( App[ None ] ):

    TITLE = "Test Issue 1122"

    BINDINGS = [
        ( "s", "toggle( 'side' )", "Sidebar" ),
        ( "b", "toggle( 'bottom' )", "Bottombar" ),
    ]

    CSS = """

    #Screen {
        layout: grid;
        grid-size: 2 5;
    }

    #main-pane {
        layout: grid;
        grid-size: 2;
    }

    .main {
        column-span: 1;
    }

    .box {
        height: 100%;
        border: round white;
        transition: offset 500ms in_out_cubic;
    }

    #sidebar {
        display: none;
        border: round yellow;
        dock: left;
        max-width: 33%;
        offset-x: -100%;
    }

    #sidebar.shown {
        display: block;
        offset-x: 0;
    }

    #bottombar {
        display: none;
        border: round red;
        dock: bottom;
        max-height: 33%;
        offset-y: 100%
    }

    #bottombar.shown {
        display: block;
        offset-y: 0;
    }
    """

    def compose(self) -> ComposeResult:
        yield Header()
        yield Container(
            Container(
                Container(
                    Static( classes="main box", id="left-main" ),
                    Static( classes="main box", id="right-main" ),
                    id="main-pane"
                ),
                Static( classes="box", id="bottombar" ),
                id="right-pane"
            ),
            Static( classes="box", id="sidebar" )
        )
        yield Footer()

    def action_toggle( self, bar: str ) -> None:
        self.query_one( f"#{bar}bar" ).toggle_class( "shown" )

if __name__ == "__main__":
    Issue1122().run()
