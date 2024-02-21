"""https://github.com/Textualize/textual/issues/2854"""

from textual import on
from textual.app import App, ComposeResult
from textual.containers import Vertical, VerticalScroll
from textual.widgets import Button, Label


class SelfRemovingLabel(Label):

    def on_mount(self) -> None:
        self.set_timer(2, self.remove)


class RemoveOnTimerApp(App[None]):

    CSS = """
    Label {
        margin-bottom: 1;
        width: 1fr;
        border: solid $warning;
        background: $warning 20%;
    }
    """

    def compose(self) -> ComposeResult:
        with Vertical():
            yield Button("Add self-removing label")
            yield VerticalScroll()

    @on(Button.Pressed)
    def add_ephemeral_label(self):
        self.query_one(VerticalScroll).mount(SelfRemovingLabel("I will remove myself!"))


if __name__ == "__main__":
    RemoveOnTimerApp().run()

### remove_on_timer.py ends here
