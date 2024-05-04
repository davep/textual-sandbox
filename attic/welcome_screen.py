"""Example of a welcome screen with timeout."""

from textual.app import App, ComposeResult
from textual.screen import Screen
from textual.widgets import Label


class Welcome(Screen):
    def compose(self) -> ComposeResult:
        yield Label("WELCOME!")

    def on_mount(self) -> None:
        self.set_timer(0.8, self.app.pop_screen)


class WelcomeScreenApp(App[None]):
    def compose(self) -> ComposeResult:
        yield Label("This is the main screen, you'll see it in a second")

    def on_mount(self) -> None:
        self.push_screen(Welcome())


if __name__ == "__main__":
    WelcomeScreenApp().run()

### welcome_screen.py ends here
