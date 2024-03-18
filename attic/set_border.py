"""An example of setting the border title from an event."""

from textual.app import App, ComposeResult
from textual.containers import Horizontal
from textual.widgets import Button


class SetBorderApp(App[None]):
    CSS = """
    Horizontal {
        border: panel cornflowerblue;
    }
    """

    def compose(self) -> ComposeResult:
        with Horizontal():
            yield Button("Set title to 'Hello'", id="Hello")
            yield Button("Set title to 'Goodbye'", id="Goodbye")

    def on_button_pressed(self, event: Button.Pressed) -> None:
        self.query_one(Horizontal).border_title = event.button.id


if __name__ == "__main__":
    SetBorderApp().run()

### set_border.py ends here
