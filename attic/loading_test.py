"""https://github.com/Textualize/textual/issues/3517"""

from textual.app import App, ComposeResult
from textual.containers import Grid, Container


class BusyBox(Container, can_focus=True):

    DEFAULT_CSS = """
    BusyBox {
        border: panel red;
    }
    BusyBox:focus {
        border: panel green;
    }
    """

    def __init__(self, number: int) -> None:
        super().__init__()
        self.border_title = f"Busy box {number}"
        self.loading = bool(number % 3)


class LoadingApp(App[None]):

    CSS = """
    Grid {
        grid-size: 4;
    }
    """

    def compose(self) -> ComposeResult:
        with Grid():
            for n in range(16):
                yield BusyBox(n)


if __name__ == "__main__":
    LoadingApp().run()

### loading_test.py ends here
