from textual.app import App, ComposeResult
from textual.containers import Horizontal, VerticalScroll
from textual.widgets import Static


class ScrollingExampleApp(App[None]):

    CSS = """
    VerticalScroll {
        border: green solid 50%;
    }

    VerticalScroll:focus {
        border: green double;
    }
    """

    def compose(self) -> ComposeResult:
        with Horizontal():
            for _ in range(4):
                with VerticalScroll():
                    yield Static("\n".join(f"Line {n}" for n in range(500)))


if __name__ == "__main__":
    ScrollingExampleApp().run()
