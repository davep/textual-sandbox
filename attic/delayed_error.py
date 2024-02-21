from textual.app import App, ComposeResult
from textual.widgets import Static
from textual.containers import Container


class Question(Container):

    def __init__(self, error_out: bool) -> None:
        self.error_out = error_out
        super().__init__()

    def compose(self) -> ComposeResult:
        wut = 1 / int(not self.error_out)
        yield Static(f"How did I get here? ({wut})")


class Crashy(App):

    def compose(self) -> ComposeResult:
        yield Question(False)
        yield Question(True)


Crashy().run()
