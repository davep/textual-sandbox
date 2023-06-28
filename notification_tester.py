from __future__ import annotations

from subprocess import run

from rich.text import Text

from textual import on
from textual.app import App, ComposeResult
from textual.containers import Grid
from textual.reactive import var
from textual.screen import Screen
from textual.widgets import Button, RadioSet, RadioButton
from textual.widgets.toast import ToastSeverityLevel

def darwin_notify(
    message: str,
    title: str | None = None,
    level: ToastSeverityLevel = "information",
    timeout: float | None = None,
) -> None:
    del level
    del timeout
    title =  f' with title "{title}"' if title else ""
    run([
        "osascript",
        "-e"
        f'display notification "{Text.from_markup(message)}"{title}'
    ])

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
            yield RadioSet(
                RadioButton("Notify Via Textual", value=True),
                RadioButton("Notify Via macOS")
            )
            for _ in range(24):
                yield Button("Press for a \nnotification")

    def on_mount(self) -> None:
        for button in self.query(Button):
            button.tooltip = "Look at this! This is a tooltip for this button!\nCool huh?"

    @on(RadioSet.Changed)
    def set_output(self, event: RadioSet.Changed) -> None:
        Screen.notifier = None if event.index == 0 else darwin_notify

    @on(Button.Pressed)
    def show_toast(self) -> None:
        self.notify(
            f"This is test notification {self.notification} :smile:\n\n:poop: :poop: :poop: :poop: :poop: :poop: :poop: :poop:",
            level=["information", "warning", "error"][self.notification % 3],
            timeout=10,
            title=[
                "This was a triumph",
                "But there's no sense crying over every mistake",
                "Anyway, this cake is great"
            ][self.notification % 3],
        )
        self.notification += 1

if __name__ == "__main__":
    NotificationTesterApp().run()
