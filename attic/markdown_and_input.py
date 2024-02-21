from textual.app import App, ComposeResult
from textual.containers import Vertical
from textual.widgets import Input, Markdown


class InputAndMarkdownApp(App[None]):

    CSS = """
    Markdown {
        margin: 0;
    }

    Input {
        border: wide $background;
        padding: 1 2;
    }

    Input:focus {
        border: wide $accent;
    }
    """

    def compose(self) -> ComposeResult:
        with Vertical():
            yield Markdown("# Here is some markdown!")
            yield Input(placeholder="Here is an input")
            yield Markdown("# Here is some markdown!")
            yield Input(placeholder="Here is an input")
            yield Markdown("# Here is some markdown!")
            yield Input(placeholder="Here is an input")
            yield Markdown("# Here is some markdown!")
            yield Input(placeholder="Here is an input")
            yield Markdown("# Here is some markdown!")
            yield Input(placeholder="Here is an input")


if __name__ == "__main__":
    InputAndMarkdownApp().run()
