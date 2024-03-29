from textual.app import App, ComposeResult, RenderResult
from textual.reactive import reactive
from textual.widgets import Static, Pretty


class Counter(Static):

    TARGET = 100

    counter1: reactive[int] = reactive(0)
    counter2: reactive[int] = reactive(0)

    def render(self) -> RenderResult:
        return (
            f"{self.counter1}\n"
            f"{'=' * int((self.size.width / self.TARGET) * self.counter1)}\n\n"
            f"{self.counter2}\n"
            f"{'=' * int((self.size.width / self.TARGET) * self.counter2)}"
        )

    def count1_complete(self) -> None:
        self.notify("TADA!", title="counter1")

    def count1(self) -> None:
        if self.counter1 in (0, self.TARGET):
            self.animate(
                "counter1",
                value=0 if self.counter1 else self.TARGET,
                duration=10,
                on_complete=self.count1_complete,
            )
        else:
            self.call_next(self.stop_animation, "counter1")

    def count2_complete(self) -> None:
        self.notify("TADA!", title="counter2")

    def count2(self) -> None:
        if not self.app._animator._scheduled:
            self.animate(
                "counter2",
                value=0 if self.counter2 else self.TARGET,
                duration=10,
                delay=10,
                on_complete=self.count2_complete,
            )
        else:
            self.call_next(self.stop_animation, "counter2")


class AnimationExplorerExample(App[None]):

    BINDINGS = [
        ("1", "count1"),
        ("2", "count2"),
    ]

    def on_mount(self) -> None:
        self.set_interval(0.2, self.show_animations)

    def show_animations(self) -> None:
        self.query_one(Pretty).update(
            {
                "_animations": self._animator._animations,
                "_scheduled": self._animator._scheduled,
            }
        )

    def compose(self) -> ComposeResult:
        yield Counter()
        yield Pretty({})

    def action_count1(self) -> None:
        self.query_one(Counter).count1()

    def action_count2(self) -> None:
        self.query_one(Counter).count2()


if __name__ == "__main__":
    AnimationExplorerExample().run()
