"""https://github.com/Textualize/textual/issues/3460"""

from textual.app import App, ComposeResult
from textual.widgets import Label

class ShowHideLabel(Label):

    def on_show(self) -> None:
        self.notify("Show!")

    def on_hide(self) -> None:
        self.notify("Hide!")

class ShowHideApp(App[None]):

    BINDINGS = [("space", "toggle")]

    def compose(self) -> ComposeResult:
        yield ShowHideLabel("Here I am")

    def action_toggle(self) -> None:
        self.query_one(ShowHideLabel).visible = not self.query_one(ShowHideLabel).visible

if __name__ == "__main__":
    ShowHideApp().run()

### show_hide.py ends here
