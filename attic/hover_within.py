"""Experimenting with hover-within, kinda."""

from textual import on
from textual.app import App, ComposeResult
from textual.containers import Vertical
from textual.events import Enter, MouseMove
from textual.widgets import Label


class MouseWatcher(Vertical):
    DEFAULT_CSS = """
    MouseWatcher {
        border: solid red;
        &.has-mouse {
            border: solid green;
            background: $boost;
        }
    }
    """

    @on(Enter)
    def mouse_grab(self) -> None:
        self.capture_mouse(True)

    @on(MouseMove)
    def refresh_mouse_status(self, event: MouseMove) -> None:
        if not (
            within_me := self
            in (
                widget
                for widget, _ in self.screen.get_widgets_at(
                    event.screen_x, event.screen_y
                )
            )
        ):
            self.capture_mouse(False)
        self.set_class(within_me, "has-mouse")


class HoverWithinApp(App[None]):
    CSS = """
    Screen {
        align: center middle;
    }

    MouseWatcher {
        width: 80%;
        height: 80%;
    }

    Label {
        border: solid yellow;
        margin: 1;
        width: 1fr;
    }
    """

    def compose(self) -> ComposeResult:
        with MouseWatcher():
            for n in range(10):
                yield Label(f"This is label {n}")


if __name__ == "__main__":
    HoverWithinApp().run()

### hover_within.py ends here
