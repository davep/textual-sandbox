"""https://github.com/Textualize/textual/discussions/4132"""

from textual import on
from textual.app import App, ComposeResult
from textual.widgets import Button, Select

class DisableSelectApp(App[None]):

    def compose(self) -> ComposeResult:
        yield Button("Disable", id="disable")
        yield Button("Enable", id="enable")
        yield Select[int]((f"This is selection {n}", n) for n in range(20))

    @on(Button.Pressed)
    def set_select_disabled(self, event: Button.Pressed) -> None:
        self.query_one(Select).disabled = event.button.id == "disable"

if __name__ == "__main__":
    DisableSelectApp().run()

### disable_select.py ends here
