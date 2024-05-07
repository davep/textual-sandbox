"""Example of submit and focus, for a question in Discord."""

from textual import on
from textual.app import App, ComposeResult
from textual.widgets import Input


class NextInputOnSubmitApp(App[None]):
    def compose(self) -> ComposeResult:
        for n in range(10):
            yield Input(placeholder=f"This is input #{n}", id=f"input-{n}")

    @on(Input.Submitted)
    def input_submitted(self, event: Input.Submitted) -> None:
        self.notify(f"The user did a submit on Input#{event.input.id}")
        self.screen.focus_next()


if __name__ == "__main__":
    NextInputOnSubmitApp().run()

### next_input.py ends here
