"""Example of using one event handler for enter or button press."""

from textual import on
from textual.app import App, ComposeResult
from textual.widgets import Button, Input


class InputAndButtonApp(App[None]):
    def compose(self) -> ComposeResult:
        yield Input()
        yield Button()

    @on(Input.Submitted)
    @on(Button.Pressed)
    def yay_the_user_submitted_a_thing(self) -> None:
        self.notify(self.query_one(Input).value, title="The Input")


if __name__ == "__main__":
    InputAndButtonApp().run()

### input_and_button.py ends here
