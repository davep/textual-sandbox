"""Example of adding to an OptionList on the fly."""

from textual import on
from textual.app import App, ComposeResult
from textual.widgets import Input, OptionList


class InputToOptionListApp(App[None]):
    def compose(self) -> ComposeResult:
        yield Input()
        yield OptionList()

    @on(Input.Submitted)
    def add_value(self, event: Input.Submitted) -> None:
        self.query_one(OptionList).add_option(event.value)
        event.control.value = ""


if __name__ == "__main__":
    InputToOptionListApp().run()

### input_to_option_list.py ends here
