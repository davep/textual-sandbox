"""Don't ask."""

from itertools import cycle, chain

from textual.app import App
from textual.widgets import Sparkline


class SparklineApp(App[None]):

    CSS = """
    Sparkline {
        &> .sparkline--max-color {
            color: red;
        }
        &> .sparkline--min-color {
            color: green;
        }
    }
    """

    STEPS = (
        lambda n: range(n + 1),
        lambda n: range((n * 2) + 1),
        lambda n: range((n * 3) + 1),
        lambda n: range((n * 4) + 1),
        lambda n: range((n * 8) + 1),
        lambda n: range((n * 16) + 1),
        lambda n: range((n * 32) + 1),
        lambda n: range((n * 64) + 1),
    )

    PATTERN = cycle(chain(STEPS, reversed(STEPS)))

    def sparks(self) -> None:
        # Dodgy, buggy, fun.
        pattern = next(self.PATTERN)
        lines = list(self.query(Sparkline))
        top = lines[: len(lines) // 2]
        tail = reversed(lines[len(lines) // 2 :])
        for n, line in enumerate(zip(top, tail)):
            line[0].data = list(pattern(n))
            line[1].data = list(pattern(n))

    async def on_resize(self) -> None:
        await self.query(Sparkline).remove()
        await self.mount_all(Sparkline([0]) for _ in range(self.size.height))

    def on_mount(self) -> None:
        self.set_interval(0.05, self.sparks)


if __name__ == "__main__":
    SparklineApp().run()

### sparkline_art.py ends here
