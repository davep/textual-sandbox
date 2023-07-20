from textual.app import App, ComposeResult, RenderResult
from textual.reactive import reactive
from textual.widgets import Static

class Counter(Static):

    TARGET = 100

    counter: reactive[int] = reactive(0)

    def render(self) -> RenderResult:
        return f"{self.counter}\n{'=' * int((self.size.width / self.TARGET) * self.counter)}"

    def count(self) -> None:
        if self.counter in (0, self.TARGET):
            self.animate(
                "counter",
                value = 0 if self.counter else self.TARGET,
                duration = 10
            )
        else:
            self.app.bell()

class AnimationExplorerExample(App[None]):

    BINDINGS = [
        ("space", "count"),
    ]

    def compose(self) -> ComposeResult:
        yield Counter()

    def action_count(self) -> None:
        self.query_one(Counter).count()

if __name__ == "__main__":
    AnimationExplorerExample().run()
