"""https://github.com/Textualize/textual/discussions/4089"""

from random import choice
from string import ascii_uppercase

from textual.app import App, ComposeResult
from textual.widgets import Static

class HoverLettersApp(App[None]):

    CSS = """
    Static {
        link-style: none;
        link-color-hover: white;
        link-background-hover: red;
    }
    """

    def compose(self) -> ComposeResult:
        text = ""
        for _ in range(5000):
            letter = choice(ascii_uppercase)
            text += f"[@click=does_nothing('{letter}')]{letter}[/]"
        yield Static(text)

    def action_does_nothing(self) -> None:
        pass


if __name__ == "__main__":
    HoverLettersApp().run()

### hover_letters.py ends here
