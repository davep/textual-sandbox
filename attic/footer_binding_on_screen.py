from textual.app import App, ComposeResult
from textual.binding import Binding
from textual.containers import Vertical
from textual.reactive import reactive
from textual.screen import Screen
from textual.widgets import Header, Footer, Label, Input, Button


class MyVert(Vertical, inherit_bindings=False):
    pass


class Game(Screen):

    BINDINGS = [
        Binding("up", "up(1)", "Press to get the highest score! (Screen)"),
        Binding("right", "up(2)", "Press to get the highest score! (Screen)"),
    ]

    score: reactive[int] = reactive(0)

    def compose(self) -> ComposeResult:
        yield Header()
        yield Label()
        yield Input()
        yield Button()
        yield Footer()

    def action_up(self, by_count: int) -> None:
        self.score += by_count
        self.query_one(Label).update(f"Score: {self.score}")


class FooterBindingOnScreen(App[None]):

    def on_mount(self) -> None:
        self.push_screen(Game())


if __name__ == "__main__":
    FooterBindingOnScreen().run()
