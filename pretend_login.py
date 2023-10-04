"""Simple example of a background login screen."""

from time import sleep
from dataclasses import dataclass

from textual import on, work
from textual.app import App, ComposeResult
from textual.message import Message
from textual.containers import Vertical, Horizontal
from textual.widgets import Button, Label, Input

class PretendLoginApp(App[None]):

    CSS = """
    Screen {
        align: center middle;
    }

    #login-dialog {
        border: panel cornflowerblue;
        width: auto;
        height: auto;
        padding: 2 4;
    }

    #login-dialog Input {
        width: 60;
    }

    #login-dialog Horizontal {
        margin-top: 1;
        height: auto;
        width: auto;
    }

    Button {
        margin-right: 1;
    }
    """

    def compose(self) -> ComposeResult:
        with Vertical(id="login-dialog"):
            yield Label("User Name:")
            yield Input(id="name")
            yield Label("Password:")
            yield Input(password=True, id="password")
            with Horizontal():
                yield Button("Login", id="login")
                yield Button("Cancel", id="cancel")

    @on(Button.Pressed, "#login")
    def login(self, event: Button.Pressed) -> None:
        event.button.label = "Wait..."
        event.button.disabled = True
        self.perform_login()

    @on(Button.Pressed, "#cancel")
    def cancel(self) -> None:
        self.exit()

    @dataclass
    class LoginResult(Message):
        okay: bool

    @work(thread=True)
    def perform_login(self) -> None:
        sleep(2)                # Let's pretend to be busy!
        self.post_message(
            self.LoginResult(
                self.query_one("#name", Input).value == "davep" and
                self.query_one("#password", Input).value == "setecastronomy"
            )
        )

    @on(LoginResult)
    def login_finished(self, result: LoginResult) -> None:
        login_button = self.query_one("#login", Button)
        login_button.label = "Login"
        login_button.disabled = False
        if result.okay:
            self.notify("YAY WE LOGGED IN!")
        else:
            self.notify("You forgot your password dummy!", severity="error")

if __name__ == "__main__":
    PretendLoginApp().run()

### pretend_login.py ends here
