"""Example of using compose_add_child"""

from textual.app import App, ComposeResult
from textual.widget import Widget
from textual.widgets import Label


class Wrapper(Widget):
    def __init__(self) -> None:
        super().__init__()
        self._other_stuff: list[Widget] = []

    def compose_add_child(self, widget: Widget) -> None:
        self._other_stuff.append(widget)

    def compose(self) -> ComposeResult:
        yield Label("Begin!")
        yield from self._other_stuff
        yield Label("End")


class AddChildApp(App[None]):
    def compose(self) -> ComposeResult:
        with Wrapper():
            yield Label("It doesn't have to be")
            yield Label("that way.")


if __name__ == "__main__":
    AddChildApp().run()

### compose_child.py ends here
