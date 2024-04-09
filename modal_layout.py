"""Example of layout differences for modals.

For a question on Discord.
"""

from textual.app import App, ComposeResult
from textual.containers import Vertical
from textual.screen import ModalScreen
from textual.widgets import Label


class SomeDialogThing(Vertical):
    DEFAULT_CSS = """
    SomeDialogThing {
        width: 50%;
        height: 50%;
        border: solid cornflowerblue;
    }
    """

    def compose(self) -> ComposeResult:
        yield Label("Press escape to close me")


class AlignedModal(ModalScreen[None]):
    DEFAULT_CSS = """
    AlignedModal {
        align: center middle;
    }
    """

    BINDINGS = [
        ("escape", "dismiss", "help"),
    ]

    def compose(self) -> ComposeResult:
        yield SomeDialogThing()


class NotAlignedModal(ModalScreen[None]):
    BINDINGS = [
        ("escape", "dismiss", "help"),
    ]

    def compose(self) -> ComposeResult:
        yield SomeDialogThing()


class ModalLayoutApp(App[None]):
    BINDINGS = [
        ("0", "not_aligned"),
        ("1", "aligned"),
    ]

    def compose(self) -> ComposeResult:
        yield Label("0 for screen with no alignment, 1 for screen with alignment")

    def action_not_aligned(self) -> None:
        self.push_screen(NotAlignedModal())

    def action_aligned(self) -> None:
        self.push_screen(AlignedModal())


if __name__ == "__main__":
    ModalLayoutApp().run()

### modal_layout.py ends here
