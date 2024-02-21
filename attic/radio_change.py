"""Example of changing a radioset's button's label."""

from textual.app import App, ComposeResult
from textual.widgets import RadioSet, RadioButton


class RadioLabelsApp(App[None]):

    BINDINGS = [("s", "swap")]

    def compose(self) -> ComposeResult:
        yield RadioSet(RadioButton("Alpha", id="one"), RadioButton("Beta", id="two"))

    def action_swap(self) -> None:
        self.query_one("#one", RadioButton).label = "Gamma"
        self.query_one("#two", RadioButton).label = "Delta"


if __name__ == "__main__":
    RadioLabelsApp().run()

### radio_change.py ends here
