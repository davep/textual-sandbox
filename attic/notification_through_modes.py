from textual.app import App, ComposeResult
from textual.reactive import var
from textual.screen import Screen
from textual.widgets import Label


class Mode(Screen):

    def __init__(self, mode: int) -> None:
        super().__init__()
        self._mode = mode

    def compose(self) -> ComposeResult:
        yield Label(f"This is mode {self._mode}")


class NotificationAndModeApp(App[None]):

    BINDINGS = [
        ("space", "show_toast"),
        ("1", "switch_mode('one')"),
        ("2", "switch_mode('two')"),
        ("3", "switch_mode('three')"),
        ("4", "switch_mode('four')"),
        ("5", "switch_mode('five')"),
    ]

    MODES = {
        "one": Mode(1),
        "two": Mode(2),
        "three": Mode(3),
        "four": Mode(4),
        "five": Mode(5),
    }

    notification: var[int] = var(0)

    def action_show_toast(self) -> None:
        self.app.notify(
            f"This is test notification {len(self.app._screen_stack)}-{self.notification} :smile: "
            * ((self.notification % 2) + 1),
            severity=["information", "warning", "error"][self.notification % 3],
            title=[
                "This was a triumph",
                "But there's no sense crying over every mistake",
                "Anyway, this cake is great",
            ][self.notification % 3],
            timeout=5,
        )
        self.notification += 1

    def on_mount(self) -> None:
        self.push_screen(Mode(0))

    def action_switch_mode(self, mode: str) -> None:
        self.switch_mode(mode)


if __name__ == "__main__":
    NotificationAndModeApp().run()
