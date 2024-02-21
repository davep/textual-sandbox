from rich.text import Text

from textual.app import App, ComposeResult
from textual.widgets import Label, Header


class MarkupTitle(App[None]):

    TITLE = str(Text.from_markup("This is the title :smile:"))

    def compose(self) -> ComposeResult:
        yield Header()
        yield Label("Hello")


if __name__ == "__main__":
    MarkupTitle().run()
