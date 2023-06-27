from textual import on
from textual.app import App, ComposeResult
from textual.containers import Grid
from textual.reactive import var
from textual.widgets import Button, Toast
from textual.widgets._toast import Rack

class NotificationTesterApp(App[None]):

    CSS = """
    Grid {
        grid-size: 5;
    }

    Button {
        width: 99%;
        height: 1fr;
    }
    """

    notification: var[int] = var(0)

    def compose(self) -> ComposeResult:
        yield Rack()
        with Grid():
            for n in range(25):
                yield Button(f"Notification {n}", id=f"b{n}")

    @on(Button.Pressed)
    def show_toast(self, event: Button.Pressed) -> None:
        self.query_one(Rack).add_toast(f"This is {self.notification}")
        self.notification += 1

if __name__ == "__main__":
    NotificationTesterApp().run()
