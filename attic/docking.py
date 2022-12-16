from inspect import cleandoc
from textual.app import App, ComposeResult
from textual.widgets import Static

class Dock( Static ):
    pass

class Docking( App[ None ] ):

    BINDINGS = [
        ( "up", "toggle('top')", "" ),
        ( "right", "toggle('right')", "" ),
        ( "down", "toggle('bottom')", "" ),
        ( "left", "toggle('left')", "" ),
    ]

    CSS = """
    Dock {
        display: none;
    }

    .visible {
        display: block;
    }

    #top {
        background: red;
        height: 30%;
        width: 100%;
        dock: top;
    }

    #left {
        background: green;
        width: 30%;
        height: 100%;
        dock: left;
    }

    #bottom {
        color: black;
        background: yellow;
        height: 30%;
        width: 100%;
        dock: bottom;
    }

    #right {
        color: black;
        background: orange;
        width: 30%;
        height: 100%;
        dock: right;
    }

    #inner {
        border: solid grey;
    }
    """

    def compose( self ) -> ComposeResult:
        yield Dock( "I am the top dock", id="top" )
        yield Dock( "I am the left dock", id="left" )
        yield Dock( "I am the bottom dock", id="bottom" )
        yield Dock( "I am the right dock", id="right" )
        yield Static( cleandoc( """
        At 0946 GMT on the morning of September 11 in the exceptionally
        beautiful summer of the year 2077, most of the inhabitants of Europe
        saw a dazzling fireball appear in the eastern sky. Within seconds it
        was brighter than the Sun, and as it moved across the heavens -- at
        first in utter silence -- it left behind it a churning column of dust
        and smoke.
        """ ) * 200, id="inner" )

    def action_toggle( self, dock: str ) -> None:
        self.query_one( f"#{dock}", Dock ).toggle_class( "visible" )

if __name__ == "__main__":
    Docking().run()

