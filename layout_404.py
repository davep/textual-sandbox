from textual.app import App, ComposeResult
from textual.containers import Container, Horizontal

class Layout404( App[ None ] ):

    CSS = """
    Container {
        background: #333;
        border: #888;
    }

    #left {
        border: none;
        width: 2fr
    }

    #right {
        border: none;
        width: 8fr;
    }

    #left-top, #left-bottom {
        height: 1fr;
    }

    #right-top {
        height: 1fr;
    }

    #right-bottom {
        height: 1;
    }
    """

    def compose(self) -> ComposeResult:
        yield Horizontal(
            Container(
                Container( id="left-top" ),
                Container( id="left-bottom" ),
                id="left"
            ),
            Container(
                Container( id="right-top" ),
                Container( id="right-bottom" ),
                id="right"
            )
        )

if __name__ == "__main__":
    Layout404().run()

