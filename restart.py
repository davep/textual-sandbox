"""Example of 'reloading' a Textual app.

For a question on Discord.
"""

from textual.app import App, ComposeResult
from textual.widgets import Button


class RestartApp(App[bool]):
    def compose(self) -> ComposeResult:
        yield Button("Restart Me", id="restart")
        yield Button("Close Me", id="close")

    def on_button_pressed(self, event: Button.Pressed) -> None:
        self.exit(event.button.id == "restart")


if __name__ == "__main__":
    while True:
        if not RestartApp().run():
            break

### restart.py ends here
