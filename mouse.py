"""Show mouse events."""

from textual import on
from textual.app import App, ComposeResult
from textual.events import MouseEvent
from textual.widgets import Log

class MouseEventLogApp(App[None]):

    def compose(self) -> ComposeResult:
        yield Log()

    @on(MouseEvent)
    def on_mouse(self, event: MouseEvent) -> None:
        self.query_one(Log).write_line(f"{event!r}")

if __name__ == "__main__":
    MouseEventLogApp().run()

### mouse.py ends here
