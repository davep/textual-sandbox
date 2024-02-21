"""Bindings showing at different levels."""

from textual.app import App, ComposeResult
from textual.containers import Vertical
from textual.screen import Screen, ModalScreen
from textual.widgets import Footer


class Child(ModalScreen):

    DEFAULT_CSS = """
    Child {
        align: center middle;
        Vertical {
            border: solid red;
            width: 80%;
            height: 80%;
        }
    }
    """

    BINDINGS = [
        ("d", "d", "Child"),
        ("e", "e", "Child"),
        ("f", "f", "Child"),
    ]

    def compose(self) -> ComposeResult:
        with Vertical():
            yield Footer()


class Main(Screen):

    BINDINGS = [
        ("a", "a", "Main"),
        ("b", "b", "Main"),
        ("c", "c", "Main"),
    ]

    def compose(self) -> ComposeResult:
        yield Footer()

    def on_mount(self) -> None:
        self.app.push_screen(Child())


class BindingsInSubScreensApp(App[None]):

    def on_mount(self) -> None:
        self.push_screen(Main())


if __name__ == "__main__":
    BindingsInSubScreensApp().run()

### screen_footer.py ends here
