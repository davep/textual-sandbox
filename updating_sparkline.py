from random import randint
from textual.app import App, ComposeResult
from textual.widgets import Sparkline


class SparklineBasicApp(App[None]):

    def compose(self) -> ComposeResult:
        yield Sparkline(
            data=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
            summary_function=max,
        )

    def on_mount(self):
        self.set_interval(0.25, self.update)

    def update(self):
        self.query_one(Sparkline).data = [
            randint(0, 9) for _ in range(10)
        ]

if __name__ == "__main__":
    SparklineBasicApp().run()

### updating_sparkline.py ends here
