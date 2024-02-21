"""https://github.com/Textualize/textual/issues/1897"""

from rich.segment import Segment
from textual.app import App, ComposeResult
from textual.widgets import Header, Footer
from textual.scroll_view import ScrollView
from textual.geometry import Size
from textual.strip import Strip


class ScrollViewTest(ScrollView, can_focus=True):

    def __init__(self, height: int) -> None:
        super().__init__()
        self.virtual_size = Size(0, height)

    def render_line(self, y: int) -> Strip:
        return Strip(
            [
                Segment(f"{self.scroll_offset.y + y:10}"),
                Segment(f"{y:10}"),
                *(
                    [Segment(f"{' ' * 10}scroll_offset.y == {self.scroll_offset.y}")]
                    if y == 0
                    else []
                ),
            ]
        )


class ScrollTestApp(App[None]):

    def compose(self) -> ComposeResult:
        yield Header()
        yield ScrollViewTest(1000)
        yield Footer()

    def on_mount(self) -> None:
        self.query_one(ScrollViewTest).focus()


if __name__ == "__main__":
    ScrollTestApp().run()

### scroll_api_test.py ends here
