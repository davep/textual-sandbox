from textual import work
from textual.app import App, ComposeResult
from textual.widgets import Label, Button


class ExitWithRunningThreadWorkerApp(App[None]):

    def compose(self) -> ComposeResult:
        yield Label()
        yield Button("Exit")

    def on_button_pressed(self) -> None:
        self.exit()

    def on_mount(self) -> None:
        self.busy_work()

    @work(thread=True)
    def busy_work(self) -> None:
        n = 0

        def _update(n) -> None:
            self.query_one(Label).update(str(n))

        while True:
            self.call_from_thread(_update, n)
            n += 1


if __name__ == "__main__":
    ExitWithRunningThreadWorkerApp().run()
