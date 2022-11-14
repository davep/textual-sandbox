from textual.app import App, ComposeResult
from textual.widgets import Header, Static
from textual.widgets._header import HeaderTitle
from textual.screen import Screen
from textual import events

class Another( Screen ):

    def compose(self):
        yield Header()
        yield Static(
            "\n".join( str( s ) for s in reversed( self.app.screen_stack ) )
        )

    def on_mount( self ):
        self.query_one(
            HeaderTitle
        ).text = f"Screen {len(self.app.screen_stack)}"


class MyApp( App[ None ] ):

    TITLE = "This is the default app screen"

    def compose( self ) -> ComposeResult:
        yield Header()
        yield Static(
            "\n".join( str( s ) for s in reversed( self.app.screen_stack ) )
        )

    def on_key(self, event: events.Key ) -> None:
        if event.key_name == "a":
            self.push_screen(
                Another( id=f"screen-{len(self.app.screen_stack)}" )
            )
        elif event.key_name =="q":
            self.pop_screen()

if __name__ == "__main__":
    MyApp().run()

