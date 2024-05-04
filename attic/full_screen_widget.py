"""Full screen toggle for widgets example."""

from pathlib import Path

from textual import on
from textual.app import App, ComposeResult
from textual.events import DescendantBlur
from textual.widgets import TextArea


class FullScreenExampleApp(App[None]):
    BINDINGS = [
        ("f11", "full_screen"),
    ]

    CSS = """
    Screen {
        layers: base fullscreen;
    }

    .fullscreen {
        layer: fullscreen;
    }
    """

    def compose(self) -> ComposeResult:
        yield TextArea(Path(__file__).read_text(), language="python")
        yield TextArea("Hey look another text area!")
        yield TextArea('(princ "Why doesn\'t TextArea support Lisp?")')

    def action_full_screen(self) -> None:
        if self.focused is not None:
            self.focused.toggle_class("fullscreen")

    @on(DescendantBlur)
    def clear_fullscreen(self, event: DescendantBlur) -> None:
        event.control.remove_class("fullscreen")


if __name__ == "__main__":
    FullScreenExampleApp().run()

### full_screen_widget.py ends here
