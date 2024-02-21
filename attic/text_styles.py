"""https://github.com/Textualize/textual/issues/2178"""

from textual.app import App, ComposeResult
from textual.containers import Horizontal, Vertical
from textual.widgets import Header, Footer, Label


class TextMarkupApp(App[None]):

    CSS = """
    Vertical {
        border: round $error;
        width: 1fr;
    }

    .bold {
        text-style: bold;
    }

    .italic {
        text-style: italic;
    }

    .underline {
        text-style: underline;
    }
    """

    def compose(self) -> ComposeResult:
        yield Header()
        with Horizontal():
            with Vertical(id="markup") as box:
                box.border_title = "Using Rich Markup"
                yield Label("[bold]Here is some bold text.[/]")
                yield Label("[italic]Here is some italic text.[/]")
                yield Label("[underline]Here is some under text.[/]")
            with Vertical(id="css") as box:
                box.border_title = "Using CSS"
                yield Label("Here is some bold text.", classes="bold")
                yield Label("Here is some italic text.", classes="italic")
                yield Label("Here is some underline text.", classes="underline")
        yield Footer()


if __name__ == "__main__":
    TextMarkupApp().run()
