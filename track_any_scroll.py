"""Example of tracking any form of scrolling.

For a question on Discord.
"""

from textual.app import App, ComposeResult
from textual.containers import Horizontal, VerticalScroll
from textual.widgets import RichLog, Label

class Scroller(VerticalScroll):

    BORDER_TITLE = "Scroller"

    def compose(self) -> ComposeResult:
        for n in range(500):
            yield Label(f"This is line number {n} in the content of this scroller")

    def _scroll_to(self, *args, **kwargs) -> bool:
        self.screen.query_one(RichLog).write("Scrolling happened!")
        return super()._scroll_to(*args, **kwargs)


class TrackScrollApp(App[None]):

    CSS = """
    Horizontal > * {
        border: panel cornflowerblue;
    }
    """

    def compose(self) -> ComposeResult:
        with Horizontal():
            yield Scroller()
            yield RichLog()

if __name__ == "__main__":
    TrackScrollApp().run()

### track_any_scroll.py ends here
