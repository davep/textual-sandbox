from textual.app     import App, ComposeResult
from textual.widgets import Button, Label
from textual.screen  import Screen
from textual.message import Message

class MyScreen( Screen ):

    def compose( self ) -> ComposeResult:
        """Compose the child widgets."""
        yield Button( "Press me to pass a value back to the app!" )

    # Here we're making a custom message which will be sent up to the
    # parent. This will carry any data.
    class SelectionMade( Message ):

        def __init__( self, result: str ) -> None:
            super().__init__()
            self.result = result

    def on_button_pressed( self ) -> None:
        # Now, normally, if you're going to post a message, you'd do
        # self.post_message. But we're about to make this screen go away,
        # and there's an issue here; still need to work out if this is a bug
        # or intended behaviour. See here:
        #
        # https://github.com/Textualize/textual/issues/2017
        #
        # So... let's either do the sensible thing or perhaps call it
        # cheating; still to be decided. Rather than post to our own message
        # queue, we want this back on the app so.... let's post to *its*
        # message queue!
        self.app.post_message( self.SelectionMade( "Hey look here's a thing!" ) )
        # Right, payload is a way, fire and forget, we can now cease to
        # exist and not worry.
        self.app.pop_screen()

class ValueFromChildExample( App[ None ] ):

    def __init__( self ) -> None:
        super().__init__()

    def compose( self ) -> ComposeResult:
        """Compose the child widgets."""
        yield Button( "Press me to load the child screen" )
        yield Label( "I'm waiting!" )

    def on_button_pressed( self ) -> None:
        self.push_screen( MyScreen() )

    # Note the naming of this event handler, see the docs:
    #
    # https://textual.textualize.io/guide/events/#message-handlers
    #
    # Making your own events and handlers is kinda fun.
    def on_my_screen_selection_made( self, event: MyScreen.SelectionMade ):
        self.query_one( Label ).update( event.result )

if __name__ == "__main__":
    ValueFromChildExample().run()
