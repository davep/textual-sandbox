"""Example of a modal screen not being too tricky, etc.

See https://github.com/Textualize/textual/discussions/4055
"""

from textual import on
from textual.app import App, ComposeResult
from textual.containers import Vertical
from textual.screen import ModalScreen
from textual.widgets import Button, Label, ListItem, ListView


class ModalDialog(ModalScreen[None]):
    CSS = """
    ModalDialog {
        align: center middle;
        Vertical {
            border: panel cornflowerblue;
            width: 70%;
            height: 70%;
            Button {
                width: 1fr;
            }
        }
    }
    """

    def compose(self) -> ComposeResult:
        with Vertical():
            yield ListView(
                *[
                    ListItem(Label(f"This is list item in a modal screen {n}"))
                    for n in range(100)
                ]
            )
            yield Button("Close")

    @on(Button.Pressed)
    def close(self) -> None:
        self.dismiss()


class ModalScreenFocusApp(App[None]):
    def compose(self) -> ComposeResult:
        yield ListView(*[ListItem(Label(f"This is list item {n}")) for n in range(100)])

    @on(ListView.Selected)
    def show_modal(self) -> None:
        self.push_screen(ModalDialog())


if __name__ == "__main__":
    ModalScreenFocusApp().run()

### modal_focus.py ends here
