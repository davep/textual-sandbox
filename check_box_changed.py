from textual.app        import App, ComposeResult
from textual.containers import Vertical, Center
from textual.widgets    import Checkbox, TextLog

class CheckBoxTestApp( App[ None ] ):

    def compose( self ) -> ComposeResult:
        with Vertical():
            with Center():
                yield Checkbox( "Toggle me" )
            yield TextLog()

    def on_checkbox_changed( self, event: Checkbox.Changed ) -> None:
        self.query_one( TextLog ).write( f"{event!r}" )

if __name__ == "__main__":
    CheckBoxTestApp().run()
