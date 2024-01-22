from code import InteractiveConsole

from textual import on
from textual.app import App, ComposeResult
from textual.reactive import var
from textual.widgets import Button, Label

class SuspendingApp(App[None]):

    counter: var[int] = var(0)

    def compose(self) -> ComposeResult:
        yield Label()
        yield Button("Suspend")

    def update_count(self) -> None:
        self.counter += 1
        self.query_one(Label).update(str(self.counter))

    def on_mount(self) -> None:
        self.set_interval(0.5, self.update_count)

    @on(Button.Pressed)
    def test_suspend(self) -> None:
        with self.suspend():
            InteractiveConsole().interact()

if __name__ == "__main__":
    SuspendingApp().run()
