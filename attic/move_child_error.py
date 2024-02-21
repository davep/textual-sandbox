"""https://github.com/Textualize/textual/issues/1743"""

from textual.app import App, ComposeResult
from textual.containers import Vertical
from textual.widgets import Label


class MoveChildErrorApp(App[None]):

    def compose(self) -> ComposeResult:
        with Vertical():
            yield Label("It's just me!")

    def on_mount(self) -> None:
        self.query_one(Vertical).move_child(self.query_one(Label), before=0)


if __name__ == "__main__":
    MoveChildErrorApp().run()

### move_child_error.py ends here
