from json    import dumps, loads
from pathlib import Path

from textual.app        import App, ComposeResult
from textual.containers import Vertical, Horizontal
from textual.widgets    import Header, Footer, Input, Label
from textual.events     import Blur

class SimpleLiveUpdate( App[ None ] ):
    """A very simple 'live update' example.

    This app creates a series if inputs, and a series of outputs which will
    simply reflect the input when the submit key (the Enter key) is pressed
    on an `Input` field. The data is also saved when this happens too. On
    reloading the application the data will be reloaded.
    """

    CSS = """
    Vertical {
        width: 1fr;
    }

    Label {
        border: round red;
        height: 3;
        width: 100%;
    }
    """

    TEST_VALUE_COUNT = 20
    """How many input/output fields to create."""

    TEST_DATA = Path( "test-data.json" )
    """The test data will be held in a file in the current directory."""

    def compose( self ) -> ComposeResult:
        yield Header()
        yield Horizontal(
            Vertical(
                *[ Input( id=f"in-{n}", placeholder="Enter data here" ) for n in range( self.TEST_VALUE_COUNT ) ]
            ),
            Vertical(
                *[ Label( id=f"out-{n}" ) for n in range( self.TEST_VALUE_COUNT ) ]
            )
        )
        yield Footer()

    def on_input_submitted( self, event: Input.Submitted ) -> None:
        # Extract out the number of input from its ID.
        _, in_num = input.id.split( "-" )
        # Find the corresponding label in the DOM and update it.
        self.query_one( f"#out-{in_num}", Label ).update( input.value )
        # Also write the data.
        self.TEST_DATA.write_text( dumps( [ input.value for input in self.query( Input ) ] ) )

    def on_mount( self ) -> None:
        # We're starting up, is there some test data?
        if self.TEST_DATA.exists():
            # There is! Lets load it and populate the interface.
            for num, value in enumerate( loads( self.TEST_DATA.read_text() ) ):
                self.query_one( f"#in-{num}", Input ).value = value
                self.query_one( f"#out-{num}", Label ).update( value )

if __name__ == "__main__":
    SimpleLiveUpdate().run()
