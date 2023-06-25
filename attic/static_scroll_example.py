from textual.app        import App, ComposeResult
from textual.containers import VerticalScroll
from textual.widgets    import Static

class ScrollingExampleApp( App[ None ] ):

    def compose( self ) -> ComposeResult:
        with VerticalScroll():
            yield Static(
                "\n".join( f"This is line number {n} - " * 4 for n in range( 500 ) )
            )

    def on_mount( self ):
        self.set_interval( 0.25, self.query_one( VerticalScroll ).scroll_down )

if __name__ == "__main__":
    ScrollingExampleApp().run()
