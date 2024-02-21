from textual import on
from textual.app import App, ComposeResult
from textual.widgets import Button


class TheBestGameEver(App[None]):

    CSS = """
    Screen {
        align: center middle;
    }

    Button {
        width: 50%;
        height: 50%;
    }
    """

    def __init__(self) -> None:
        super().__init__()
        self.score = 0

    def compose(self) -> ComposeResult:
        yield Button(str(self.score))

    @on(Button.Pressed)
    def clicker(self) -> None:
        self.score += 1
        self.query_one(Button).label = str(self.score)


if __name__ == "__main__":
    TheBestGameEver().run()

### button_clicker.py ends here
