from textual import work
from textual.app import App, ComposeResult
from textual.widgets import Label


class TimerWorkerApp(App[None]):

    def compose(self) -> ComposeResult:
        yield Label("This will change soon.")

    def on_mount(self) -> None:
        self.set_timer(5, self.boo)  # Currently has a type error on the callable.

    @work
    async def boo(self) -> None:
        self.query_one(Label).update("BOO!")


if __name__ == "__main__":
    TimerWorkerApp().run()

### timer_worker.py ends here
