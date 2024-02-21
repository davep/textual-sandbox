"""https://github.com/Textualize/textual/discussions/3889"""

from textual.app import App, ComposeResult
from textual.containers import Horizontal, Vertical
from textual.widgets import Label


class Panel(Vertical, can_focus=True):

    DEFAULT_CSS = """
    Panel {
        border: round red;
    }

    Panel:focus {
        border: round green;
    }
    """


class BoundFocusExampleApp(App[None]):

    BINDINGS = [
        ("f1", "focus('left')"),
        ("f2", "focus('right')"),
    ]

    def compose(self) -> ComposeResult:
        with Horizontal():
            with Panel(id="left"):
                yield Label("This is the left panel (press F1)")
            with Panel(id="right"):
                yield Label("This is the right panel (press F2)")


if __name__ == "__main__":
    BoundFocusExampleApp().run()

### bound_focus.py ends here
