from typing import Any

from textual.app import App, ComposeResult
from textual.containers import Vertical
from textual.widgets import Label

class LabeledBox( Vertical ):

    DEFAULT_CSS = """
    LabeledBox {
        layers: base label;
    }

    LabeledBox Vertical {
        layer: base;
        border: solid $primary;
    }

    LabeledBox Label {
        layer: label;
        offset: 2 0;
        width: auto;
        color: orange;
    }
    """

    def __init__( self, label: str, *args: Any, **kwargs: Any ) -> None:
        self._label = label
        super().__init__( *args, **kwargs )

    def compose( self ) -> ComposeResult:
        yield Vertical()
        yield Label( self._label )

class BoxLabelTest( App[ None ] ):

    def compose( self ) -> ComposeResult:
        yield LabeledBox( "Look at this cool box!" )

if __name__ == "__main__":
    BoxLabelTest().run()
