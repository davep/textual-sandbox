"""https://github.com/Textualize/textual/discussions/1315"""

from textual.app import App, ComposeResult
from textual.containers import Horizontal
from textual.widgets import Label

class LabelAuto( App[ None ] ):

    CSS = """
    Horizontal {
        border: solid blue;
        height: auto;
    }

    Label {
        border: solid red;
    }

    .width {
        width: auto;
    }

    .height {
        height: auto;
    }

    .one-fr {
        width: 1fr;
    }
    """

    def compose(self) -> ComposeResult:
        yield Horizontal(
            Label( "Raw Label" ),
            Label( "Raw Label" ),
            Label( "Raw Label" ),
            Label( "Raw Label" ),
            Label( "Raw Label" )
        )
        yield Horizontal(
            Label( "width: auto;", classes="width" ),
            Label( "height: auto;", classes="height" ),
            Label( "width: auto; height: auto;", classes="width height" )
        )
        yield Horizontal( Label( "width: auto;", classes="width" ) )
        yield Horizontal( Label( "height: auto;", classes="height" ) )
        yield Horizontal( Label( "width: auto; height: auto;", classes="width height" ) )
        yield Horizontal(
            Label( "width: auto;", classes="width" ),
            Label( "width: auto;", classes="width" ),
            Label( "width: auto;", classes="width" )
        )
        yield Horizontal(
            Label( "width: 1fr;", classes="one-fr" ),
            Label( "width: 1fr;", classes="one-fr" )
        )
        yield Horizontal(
            Label( "width: 1fr;", classes="one-fr" ),
            Label( "width: 1fr;", classes="one-fr" ),
            Label( "width: 1fr;", classes="one-fr" ),
            Label( "width: 1fr;", classes="one-fr" ),
            Label( "width: 1fr;", classes="one-fr" ),
            Label( "width: 1fr;", classes="one-fr" )
        )

    def on_mount( self ) -> None:
        self.call_after_refresh( self.add_actual_width )

    def add_actual_width( self ) -> None:
        for label in self.query( Label ):
            label.update( f"{label.renderable} ({label.styles.width})" )

if __name__ == "__main__":
    LabelAuto().run()
