"""Example of how Header and Footer are per-screen."""

from textual.app import App, ComposeResult
from textual.screen import Screen
from textual.widgets import Footer, Header, Label


class Other(Screen):
    BINDINGS = [
        ("space", "app.pop_screen"),
    ]

    def compose(self) -> ComposeResult:
        yield Label("Press space to show the main screen")


class ScreenAndHeadersAndFootersOhMyApp(App[None]):
    BINDINGS = [
        ("space", "other_screen"),
    ]

    def compose(self) -> ComposeResult:
        yield Header()
        yield Label("Press space to show the other screen")
        yield Footer()

    def action_other_screen(self) -> None:
        self.push_screen(Other())


if __name__ == "__main__":
    ScreenAndHeadersAndFootersOhMyApp().run()

### screens_and_headers.py ends here
