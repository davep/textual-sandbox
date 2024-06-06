"""Example of an app that is light mode from the start."""

from textual.app import App, ComposeResult
from textual.widgets import Label


class LightApp(App[None]):
    def __init__(self):
        super().__init__()
        self.dark = False

    def compose(self) -> ComposeResult:
        yield Label("This is a light app")


if __name__ == "__main__":
    LightApp().run()

### light_app.py ends here
