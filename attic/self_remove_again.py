"""https://github.com/Textualize/textual/issues/2016"""

from textual.app import App, ComposeResult
from textual.containers import Vertical
from textual.widgets import Header, Footer, Button


class SelfRemoveButton(Button):

    DEFAULT_CSS = """
    SelfRemoveButton {
        width: 100%;
    }
    """

    def on_button_pressed(self):
        self.remove()


class SelfRemoveApp(App[None]):

    BINDINGS = [("a", "add", "Add a button")]

    def compose(self) -> ComposeResult:
        yield Header()
        yield Vertical()
        yield Footer()

    def action_add(self) -> None:
        self.query_one(Vertical).mount(SelfRemoveButton("Press me to remove me"))


if __name__ == "__main__":
    SelfRemoveApp().run()
