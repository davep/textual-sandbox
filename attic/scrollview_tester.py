from rich.segment import Segment

from textual.app import App, ComposeResult
from textual.widgets import Header, Footer
from textual.containers import Grid
from textual.scroll_view import ScrollView
from textual.strip import Strip
from textual.geometry import Size


class TestScrollView(ScrollView, can_focus=True):

    def __init__(self, height: int, border_title: str) -> None:
        super().__init__()
        self.virtual_size = Size(0, height)
        self.border_title = border_title

    def render_line(self, y: int) -> Strip:
        return Strip(
            [
                Segment(f"Welcome to line {self.scroll_offset.y + y}"),
            ]
        )


class ScrollViewTester(App[None]):

    CSS = """
    Grid {
        grid-size: 3;
    }

    TestScrollView {
        background: $primary-darken-2;
        border: round red;
    }

    TestScrollView:focus {
        background: $primary;
        border: double green;
    }
    """

    def compose(self) -> ComposeResult:
        yield Header()
        with Grid():
            for n in range(3 * 3):
                yield TestScrollView(height=1000, border_title=f"{n}")
        yield Footer()


if __name__ == "__main__":
    ScrollViewTester().run()
