from textual.app import App, ComposeResult
from textual.containers import Horizontal, Vertical, VerticalScroll
from textual.widgets import Header, Footer, Static


class ScreenSplitApp(App[None]):

    CSS = """
    Horizontal {
        width: 1fr;
    }

    Vertical {
        width: 1fr;
        background: red;
        min-width: 42;
    }

    VerticalScroll {
        width: 3fr;
        background: $panel;
    }

    Static {
        width: 1fr;
        content-align: center middle;
        border: double red;
    }

    Static.stripe-0 {
        background: green;
    }

    Static.stripe-1 {
        background: blue;
    }
    """

    def compose(self) -> ComposeResult:
        yield Header()
        with Horizontal():
            yield Vertical()
            with VerticalScroll():
                for n in range(500):
                    yield Static(
                        f"This is content number {n}", classes=f"stripe-{n % 2}"
                    )
        yield Footer()


if __name__ == "__main__":
    ScreenSplitApp().run()
