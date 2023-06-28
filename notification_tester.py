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

    Button {
        width: 99%;
        height: 1fr;
    }
    """

    notification: var[int] = var(0)

    def compose(self) -> ComposeResult:
        with Grid():
            for n in range(25):
                yield Button("Press for a \nnotification")

    def on_mount(self) -> None:
        for button in self.query(Button):
            button.tooltip = "Look at this! This is a tooltip for this button!\nCool huh?"

    @on(Button.Pressed)
    def show_toast(self) -> None:
        self.notify(
            f"This is [i]test[/] [b]notification[/] {self.notification} :smile:\n\n:poop: :poop: :poop: :poop: :poop: :poop: :poop: :poop:",
            level=["information", "warning", "error"][self.notification % 3],
            timeout=10
        )
        self.notification += 1

if __name__ == "__main__":
    NotificationTesterApp().run()
