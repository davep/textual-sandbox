from textual.app import App, ComposeResult
from textual.widgets import Input, Button

class EnterLeak( App[ None ] ):

    CSS = """Screen { align: center middle; }"""

    def compose(self) -> ComposeResult:
        yield Input( id="first", placeholder="Focus should go here" )
        yield Input( id="second", placeholder="Focus actually goes here" )
        yield Button( "Press me to try and focus the first field" )

    def on_input_submitted( self, event: Input.Submitted ) -> None:
        print( f"on_input_submitted( {event.input!r})" )
        if event.input.id == "first":
           self.set_focus( self.query_one( "#second" ), Input )
           print( "on_input_submitted is on the #first input and is moving to the #second input" )
        else:
           self.set_focus( self.query_one( "#first" ), Input )
           print( "on_input_submitted is on the #second input and is moving to the #first input" )

    def on_button_pressed( self, event: Button.Pressed ) -> None:
        self.set_focus( self.query_one( "#first", Input ) )

if __name__ == "__main__":
    EnterLeak().run()

