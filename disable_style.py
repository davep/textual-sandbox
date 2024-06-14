"""Example of styling disabled widgets."""

from textual import on
from textual.app import App, ComposeResult
from textual.containers import Grid
from textual.widgets import Button


class DisableStyleExampleApp(App[None]):
    CSS = """
    Grid {
        grid-size: 5;
    }

    Button {
        width: 1fr;
        height: 1fr;

        &:disabled {
            background: red;
        }
    }
    """

    def compose(self) -> ComposeResult:
        with Grid():
            for n in range(25):
                yield Button(
                    "This will disable", classes="we-can-disable-this"
                ) if n % 2 else Button("This never disables")

    @on(Button.Pressed)
    def toggle_disabled(self) -> None:
        for button in self.query(".we-can-disable-this"):
            button.disabled = not button.disabled


if __name__ == "__main__":
    DisableStyleExampleApp().run()

### disable_style.py ends here
