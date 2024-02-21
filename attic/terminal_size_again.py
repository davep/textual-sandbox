from textual.app import App, ComposeResult
from textual.containers import Vertical
from textual.widgets import Label


class TerminalSize(App[None]):

    CSS = """
    Vertical {
        width: 100%;
        height: 100%;
        border: thick red;
        align: center middle;
    }
    """

    def compose(self) -> ComposeResult:
        with Vertical():
            yield Label()

    def on_resize(self) -> None:
        self.query_one(Label).update(f"{self.size.width} x {self.size.height}")


if __name__ == "__main__":
    TerminalSize().run()
