from textual.app import App, ComposeResult
from textual.widgets import Static


class TransparentScreen(App[None]):

    CSS = """
    Screen {
        align: center middle;
    }
    Static {
        width: auto;
    }
    """

    def compose(self) -> ComposeResult:
        yield Static("Hello, World!")


if __name__ == "__main__":
    TransparentScreen().run()
