from textual.app import App, ComposeResult
from textual.containers import Vertical
from textual.screen import Screen
from textual.widget import Widget
from textual.widgets import Header, Footer, Input, Label


class TestScreen(Screen):

    def compose(self) -> ComposeResult:
        yield Header()
        yield Vertical(
            Label("I'll show the focused ID here"),
            *[Input(id=f"input-{n}", placeholder=f"Test input {n}") for n in range(10)],
        )
        yield Footer()

    def watch_focused(self, blurring: Widget, focusing: Widget) -> None:
        self.query_one(Label).update(f"Focus went from {blurring} to {focusing}")


class FocusChaner(App[None]):

    CSS = """
    Label {
        height: 3;
        width: 100%;
        border: round green;
    }
    """

    def on_mount(self) -> None:
        self.push_screen(TestScreen())


if __name__ == "__main__":
    FocusChaner().run()
