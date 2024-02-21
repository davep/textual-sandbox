from textual.app import App, ComposeResult
from textual.containers import Vertical
from textual.widgets import Header, Footer, TextLog
from textual.binding import Binding


class TextLogTester(App[None]):

    BINDINGS = [Binding(str(n), f"emit({n})", str(n)) for n in range(10)]

    def compose(self) -> ComposeResult:
        yield Header()
        yield Vertical(TextLog(highlight=True, wrap=True))
        yield Footer()

    def on_mount(self) -> None:
        self.query_one(TextLog).write("This was done on mount")

    def action_emit(self, how_many: int) -> None:
        self.query_one(TextLog).write(
            "This 'was' something that was added via an action. " * how_many
        )


if __name__ == "__main__":
    TextLogTester().run()
