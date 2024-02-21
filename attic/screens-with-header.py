from textual.app import App, ComposeResult
from textual.screen import Screen
from textual.widgets import Header, Footer, Static


class TestScreen(Screen):

    def compose(self) -> ComposeResult:
        yield Header()
        yield Static("This is a screen")
        yield Static(f"The screen stack is this big: {len(self.app.screen_stack)}")
        yield Footer()


class ScreenTest(App[None]):

    BINDINGS = [
        ("n", "new_screen", "New Screen"),
        ("r", "remove_screen", "Remove Screen"),
    ]

    def compose(self) -> ComposeResult:
        yield Header()
        yield Static("This the default screen")
        yield Static(f"The screen stack is this big: {len(self.screen_stack)}")
        yield Footer()

    def action_new_screen(self):
        self.push_screen(TestScreen())

    def action_remove_screen(self):
        self.pop_screen()


if __name__ == "__main__":
    ScreenTest().run()
