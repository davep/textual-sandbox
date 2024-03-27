"""Example of 'clicking' a RadioButton in a RadioSet from code."""

from textual.app import App, ComposeResult
from textual.widgets import RadioButton, RadioSet

NAMES = ["Sam", "Cliff", "Fragile", "Higgs", "Amelie", "Lockne"]


class RadioSetApp(App[None]):
    def compose(self) -> ComposeResult:
        yield RadioSet(*[RadioButton(name, id=name.lower()) for name in NAMES])

    def on_mount(self) -> None:
        self.query_one("#higgs", RadioButton).value = True


if __name__ == "__main__":
    RadioSetApp().run()

### click_radiobutton.py ends here
