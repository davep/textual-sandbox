from textual.app     import App, ComposeResult
from textual.widgets import ProgressBar

class ProgressTipApp( App[ None ] ):

    def compose( self ) -> ComposeResult:
        yield ProgressBar( 100 )

    def on_mount( self ) -> None:
        for part in self.query_one( ProgressBar ).query( "*" ):
            part.tooltip = "Hello from the Progress bar!"

if __name__ == "__main__":
    ProgressTipApp().run()
