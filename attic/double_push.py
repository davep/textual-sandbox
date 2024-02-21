from textual.app import App, ComposeResult
from textual.containers import Grid
from textual.screen import Screen
from textual.widgets import Header, Footer, Button, Label


class Popper(Screen):

    def compose(self) -> ComposeResult:
        """Compose the child widgets."""
        yield Label("WAIT FOR IT!")

    def on_show(self) -> None:
        self.set_timer(5.0, self.app.pop_screen)


class Main(Screen):

    def compose(self) -> ComposeResult:
        """Compose the child widgets."""
        yield Label(":-/")
        yield Button("Press me!")

    def on_show(self) -> None:
        self.app.push_screen("popper")

    def on_button_pressed(self, _: Button.Pressed):
        self.query_one(Label).update(":-D")


class DoublePush(App[None]):

    CSS = """
    Screen {
        align: center middle;
    }
    """

    SCREENS = {"main": Main, "popper": Popper}

    def compose(self) -> ComposeResult:
        yield Header()
        yield Button("Make Screen")
        yield Footer()

    def on_button_pressed(self, _: Button.Pressed):
        self.push_screen("main")


if __name__ == "__main__":
    DoublePush().run()
