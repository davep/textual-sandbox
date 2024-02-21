"""https://github.com/Textualize/textual/issues/1256"""

from textual.app import App, ComposeResult
from textual.containers import Vertical
from textual.widgets import Label


class HH(Label):

    DEFAULT_CSS = """
    HH {
        margin-top: 1;
        text-style: bold;
    }
    """


class H(HH):

    DEFAULT_CSS = """
    H {
        border: hkey red;
    }
    """


class PopOver(Vertical):

    def compose(self) -> ComposeResult:
        yield H("This Is The Title")
        yield HH("This is a sub-title")
        yield Label("This is some test under that sub-title.")
        yield HH("This is a sub-title")
        yield Label("This is some test under that sub-title.")
        yield HH("This is a sub-title")
        yield Label("This is some test under that sub-title.")


class OffsetError(App[None]):

    CSS = """
    Screen {
        layers: base popover;
    }

    PopOver {
        layer: popover;
        background: $panel;
        border: round $primary;
        height: 80%;
        width: 50%;
        offset-y: 10%;
        offset-x: 50%;
        transition: offset 250ms in_out_cubic;
    }

    PopOver.hidden {
        offset: -100% 10%;
    }
    """

    BINDINGS = [("p", "popover", "Toggle the popover")]

    def compose(self) -> ComposeResult:
        yield Vertical(H("Press P to show the popover"), PopOver(classes="hidden"))

    def action_popover(self) -> None:
        self.query_one(PopOver).toggle_class("hidden")


if __name__ == "__main__":
    OffsetError().run()
