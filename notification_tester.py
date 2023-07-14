from __future__ import annotations

from textual import on
from textual.app import App, ComposeResult
from textual.containers import Grid
from textual.reactive import var
from textual.screen import Screen
from textual.widgets import Button, Label, Footer

class NotificationScreen(Screen):

    BINDINGS = [
        ("down", "push", "Push new screen"),
        ("up", "pop", "Pop this screen"),
        ("delete", "clear")
    ]

    notification: var[int] = var(0)

    def compose(self) -> ComposeResult:
        yield Label(f"Screen depth: {len(self.app._screen_stack)}")
        with Grid():
            for _ in range(25):
                yield Button("Press for a \nnotification")
        yield Footer()

    def on_mount(self) -> None:
        for button in self.query(Button):
            button.tooltip = "Look at this! This is a tooltip for this button!\nCool huh?"
        #self.app.notify("This was raised in on_mount")

    @on(Button.Pressed)
    def show_toast(self) -> None:
        self.app.notify(
            f"This is test notification {len(self.app._screen_stack)}-{self.notification} :smile: " * ((self.notification % 2)+1),
            severity=["information", "warning", "error"][self.notification % 3],
            title=[
                "This was a triumph",
                "But there's no sense crying over every mistake",
                "Anyway, this cake is great"
            ][self.notification % 3],
            timeout=60
        )
        self.notification += 1

    def action_push(self) -> None:
        self.app.push_screen(NotificationScreen())

    def action_pop(self) -> None:
        if len(self.app._screen_stack) > 2:
            self.app.pop_screen()
        else:
            self.app.bell()

    def action_clear(self) -> None:
        self.app.clear_notifications()

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

    def on_mount(self) -> None:
        self.push_screen(NotificationScreen())

if __name__ == "__main__":
    NotificationTesterApp().run()
