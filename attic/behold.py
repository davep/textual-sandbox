"""The best new way to do Textual event handlers."""

from textual import on as behold
from textual.app import App, ComposeResult
from textual.widgets import Button


class NewEventHandlerStyleApp(App[None]):
    def compose(self) -> ComposeResult:
        yield Button()

    @behold(Button.Pressed)
    def boop(self) -> None:
        self.notify("Boop!")


if __name__ == "__main__":
    NewEventHandlerStyleApp().run()

### behold.py ends here
