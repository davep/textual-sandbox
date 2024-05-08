"""Example of submit and focus, for a question in Discord."""

from textual import on
from textual.app import App, ComposeResult
from textual.widgets import Input


class NextInputOnSubmitApp(App[None]):
    def compose(self) -> ComposeResult:
        yield Input(id="username")
        yield Input(id="password")

    @on(Input.Submitted, "#username")
    def user_name(self) -> None:
        self.notify("Cool, that's the user name")

    @on(Input.Submitted, "#password")
    def password(self) -> None:
        self.notify("Aaaaaaaand that's the password")

    @on(Input.Submitted)
    def bump_focus(self) -> None:
        self.screen.focus_next()


if __name__ == "__main__":
    NextInputOnSubmitApp().run()

### next_input.py ends here
