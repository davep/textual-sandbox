from textual.app     import App, ComposeResult
from textual.widgets import Static

class MouseReaction( Static ):

    DEFAULT_CSS = """
    MouseReaction {
        border: solid green;
        width: 50%;
        height: 50%;
    }

    MouseReaction.mouse-here {
        border: double red;
        background: yellow;
    }
    """

    def on_enter(self) -> None:
        self.set_class( True, "mouse-here" )

    def on_leave(self) -> None:
        self.set_class( False, "mouse-here" )

class MouseEnterExitApp( App[ None ] ):

    CSS = """
    Screen {
        align: center middle;
    }
    """

    def compose( self ) -> ComposeResult:
        yield MouseReaction()

if __name__ == "__main__":
    MouseEnterExitApp().run()
