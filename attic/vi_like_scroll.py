from textual.app import App, ComposeResult
from textual.containers import Grid, ScrollableContainer
from textual.widgets import Static


class ViLikeScrollableContainer(ScrollableContainer, can_focus=True):

    DEFAULT_CSS = """
    ViLikeScrollableContainer {
        border: solid red;
    }

    ViLikeScrollableContainer:focus {
        border: double green;
    }
    """

    BINDINGS = [
        ("k", "scroll_up"),
        ("j", "scroll_down"),
    ]


class ViLikeScrollingApp(App[None]):

    CSS = """
    Grid {
        grid-size: 3;
    }
    """

    def compose(self) -> ComposeResult:
        with Grid():
            for _ in range(9):
                with ViLikeScrollableContainer():
                    yield Static("\n".join(f"This is line {n}" for n in range(100)))


if __name__ == "__main__":
    ViLikeScrollingApp().run()
