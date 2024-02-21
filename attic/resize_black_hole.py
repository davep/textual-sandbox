"""https://github.com/Textualize/textual/issues/2502"""

from textual.app import App, ComposeResult
from textual.widgets import Static


class ResizeBlackHoleApp(App[None]):

    CSS = """
    Screen {
        layout: horizontal;
    }

    .fraction {
        min-width: 3;
        width: 1fr;
    }

    .fixed {
        width: 0;
    }
    """

    def compose(self) -> ComposeResult:
        for _ in range(100):
            yield Static(classes="fraction")
            yield Static(classes="fixed")


if __name__ == "__main__":
    ResizeBlackHoleApp().run()
