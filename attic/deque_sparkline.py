"""https://github.com/Textualize/textual/issues/3899"""

from collections import deque

from textual.app import App, ComposeResult
from textual.widgets import Sparkline


class SparklineBasicApp(App[None]):
    def compose(self) -> ComposeResult:
        yield Sparkline(
            deque([1, 2, 2, 1, 1, 4, 3, 1, 1, 8, 8, 2]),
            summary_function=max,
        )


if __name__ == "__main__":
    SparklineBasicApp().run()

### deque_sparkline.py ends here
