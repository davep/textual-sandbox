"""An example of reacting to the mouse entering and leaving."""

from textual.app import App, ComposeResult
from textual.widgets import Label


class MyWidget(Label):
    def watch_mouse_over(self, value: bool) -> None:
        self.update("Options" if value else "Not Options")


class EnterLeaveApp(App[None]):
    def compose(self) -> ComposeResult:
        yield MyWidget("Not Options")


if __name__ == "__main__":
    EnterLeaveApp().run()

### enter_leave.py ends here
