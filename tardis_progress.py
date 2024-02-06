"""Code for testing non-linear time progress."""

from functools import partial
from random import random
from typing import Callable

from textual import on
from textual.app import App, ComposeResult
from textual.containers import Horizontal
from textual.reactive import var
from textual.timer import Timer
from textual.widgets import Button, ProgressBar

class TardisProgressApp(App[None]):

    CSS = """
    #all {
        width: 1fr;
    }

    Horizontal {
        height: auto;
    }

    ProgressBar {
        margin: 1;
        width: 1fr;
        Bar {
            width: 1fr;
        }
    }
    """

    constant: var[int] = var(0)
    fibbonaci: var[int] = var(0)
    timers: var[dict[ProgressBar, Timer]] = var({})

    def compose(self) -> ComposeResult:
        yield Button("All", id="all")
        with Horizontal():
            yield Button("Constant 0.1", classes="constant-1")
            yield ProgressBar(classes="constant-1")
        with Horizontal():
            yield Button("Constant 0.2", classes="constant-2")
            yield ProgressBar(classes="constant-2")
        with Horizontal():
            yield Button("Constant 0.5", classes="constant-5")
            yield ProgressBar(classes="constant-5")
        with Horizontal():
            yield Button("Random", classes="random")
            yield ProgressBar(classes="random")
        with Horizontal():
            yield Button("Accelerating", classes="accelerating")
            yield ProgressBar(classes="accelerating")
        with Horizontal():
            yield Button("Decelerating", classes="decelerating")
            yield ProgressBar(classes="decelerating")
        with Horizontal():
            yield Button("Just sit at 1", classes="just-sits-there")
            yield ProgressBar(classes="just-sits-there")

    def update_progress(self, progress: ProgressBar, time_step: float, tardis: Callable[[float], float]) -> None:
        if progress in self.timers:
            self.timers[progress].stop()
        progress.progress += 1
        if progress.progress != 100:
            self.timers[progress] = self.set_timer(
                tardis(time_step),
                partial(self.update_progress, progress, tardis(time_step), tardis)
            )

    @staticmethod
    def constant_tardis(time_step: float) -> Callable[[float], float]:
        def step(_: float) -> float:
            return time_step
        return step

    def progress(self, progress: str) -> ProgressBar:
        bar = self.query_one(f"ProgressBar.{progress}", ProgressBar)
        if bar in self.timers:
            self.timers[bar].stop()
        try:
            bar.update(total=100, progress=0, reset_eta=True)
        except TypeError:
            bar.update(total=100, progress=0)
        return bar

    @on(Button.Pressed, "#all, .constant-1")
    def start_constant_progress_1(self) -> None:
        self.update_progress(self.progress("constant-1"), 0, self.constant_tardis(0.1))

    @on(Button.Pressed, "#all, .constant-2")
    def start_constant_progress_2(self) -> None:
        self.update_progress(self.progress("constant-2"), 0, self.constant_tardis(0.2))

    @on(Button.Pressed, "#all, .constant-5")
    def start_constant_progress_5(self) -> None:
        self.update_progress(self.progress("constant-5"), 0, self.constant_tardis(0.5))

    @on(Button.Pressed, "#all, .random")
    def start_random_progress(self) -> None:
        def random_tardis(_: float) -> Callable[[float], float]:
            def step(_: float) -> float:
                return random()
            return step
        self.update_progress(self.progress("random"), 0, random_tardis(0))

    @on(Button.Pressed, "#all, .accelerating")
    def start_accelerating_progress(self) -> None:
        def accelerating_tardis(_: float) -> Callable[[float], float]:
            def step(time_now: float) -> float:
                return time_now * 0.9
            return step
        self.update_progress(self.progress("accelerating"), 3, accelerating_tardis(0))

    @on(Button.Pressed, "#all, .decelerating")
    def start_decelerating_progress(self) -> None:
        def decelerating_tardis(_: float) -> Callable[[float], float]:
            def step(time_now: float) -> float:
                return time_now / 0.9
            return step
        self.update_progress(self.progress("decelerating"), 0.1, decelerating_tardis(0))

    @on(Button.Pressed, "#all, .just-sits-there")
    def start_still_progress(self) -> None:
        self.progress("just-sits-there").progress = 1

if __name__ == "__main__":
    TardisProgressApp().run()

### tardis_progress.py ends here
