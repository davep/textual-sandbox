"""https://github.com/Textualize/textual/discussions/4007"""

from textual import on
from textual.app import App, ComposeResult
from textual.reactive import var
from textual.widgets import Button


class DelayedReactiveApp(App[None]):

    _username: var[str | None] = var(None)

    @property
    def username(self) -> str:
        if self._username is None:
            raise Exception("Nope")
        return self._username

    @username.setter
    def username(self, new_username: str) -> None:
        self._username = new_username

    def compose(self) -> ComposeResult:
        yield Button("Show the username (might crash)", id="show")
        yield Button("Set the username", id="set")

    @on(Button.Pressed, "#show")
    def show_username(self) -> None:
        self.notify(self.username)

    @on(Button.Pressed, "#set")
    def set_username(self) -> None:
        self.username = "davep"
        self.notify("Username has been set")


if __name__ == "__main__":
    DelayedReactiveApp().run()

### delayed_reactive.py ends here
