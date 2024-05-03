"""Example of toasts coming in from the top."""

from textual import on
from textual.app import App, ComposeResult
from textual.widgets import Button


class ToastTopRightApp(App[None]):
    CSS = """
    ToastRack {
        align: right top;
    }
    """

    def compose(self) -> ComposeResult:
        yield Button("Boop")

    @on(Button.Pressed)
    def boop(self) -> None:
        self.notify("You booped the button!")


if __name__ == "__main__":
    ToastTopRightApp().run()

### toast_top_right.py ends here
