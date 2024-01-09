"""https://github.com/Textualize/textual/discussions/3987"""

from textual.app import App, ComposeResult
from textual.widgets import Sparkline

class SparklineApp(App[None]):

    def compose(self) -> ComposeResult:
        for n in range(40):
            yield Sparkline(list(reversed(range(n+1))))


if __name__ == "__main__":
    SparklineApp().run()

### sparkline_art.py ends here
