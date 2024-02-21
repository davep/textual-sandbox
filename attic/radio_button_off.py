"""https://discord.com/channels/1026214085173461072/1033754296224841768/1091033493762474004"""

from textual.app import App, ComposeResult
from textual.containers import Vertical
from textual.widgets import Header, Footer, RadioButton


class RBOffTestApp(App[None]):

    BINDINGS = [
        ("y", "rb( True )", "Turn radio buttons on"),
        ("n", "rb( False )", "Turn radio buttons off"),
    ]

    def compose(self) -> ComposeResult:
        yield Header()
        with Vertical():
            for n in range(20):
                yield RadioButton(f"This is RadioButton {n}", value=True)
        yield Footer()

    def action_rb(self, value: bool) -> None:
        for rb in self.query(RadioButton):
            rb.value = value


if __name__ == "__main__":
    RBOffTestApp().run()

### radio_button_off.py ends here
