from __future__ import annotations

from textual import on
from textual.app import App, ComposeResult
from textual.containers import Grid
from textual.reactive import var
from textual.widgets import Button

class NotificationTesterApp(App[None]):

    CSS = """
    Grid {
        grid-size: 5;
    }

    RadioSet {
        width: 1fr;
        height: 1fr;
    }
    Button {
        width: 99%;
        height: 1fr;
    }
    """

    notification: var[int] = var(0)

    def compose(self) -> ComposeResult:
        with Grid():
            for _ in range(25):
                yield Button("Press for a \nnotification")

    def on_mount(self) -> None:
        for button in self.query(Button):
            button.tooltip = "Look at this! This is a tooltip for this button!\nCool huh?"
        self.app.notify("This was raised in on_mount")

    @on(Button.Pressed)
    def show_toast(self) -> None:
        self.app.notify(
            f"This is test notification {self.notification} :smile:\n\n:poop: :poop: :poop: :poop: :poop: :poop: :poop: :poop:",
            severity=["information", "warning", "error"][self.notification % 3],
            title=[
                "This was a triumph",
                "But there's no sense crying over every mistake",
                "Anyway, this cake is great"
            ][self.notification % 3],
        )
        self.notification += 1

if __name__ == "__main__":
    NotificationTesterApp().run()
