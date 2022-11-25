"""https://github.com/Textualize/textual/issues/1275"""

from textual.app import App, ComposeResult
from textual.widgets import Header, Footer, Button

class HeaderTest( App[ None ] ):

    TITLE = "This is the title"
    SUB_TITLE = "This is the sub-title"

    CSS = """
    Screen {
        align: center middle;
    }
    """

    counter = 0

    def compose( self ) -> ComposeResult:
        yield Header()
        yield Button()
        yield Footer()

    def on_button_pressed( self, _: Button.Pressed ) -> None:
        self.counter += 1
        self.title = f"This is title update {self.counter}"
        self.sub_title = f"This is sub-title update {self.counter}"

if __name__ == "__main__":
    HeaderTest().run()

