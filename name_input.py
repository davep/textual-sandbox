"""Example of messages up, attributes down."""

from dataclasses import dataclass

from textual import on
from textual.app import App, ComposeResult
from textual.containers import Vertical
from textual.message import Message
from textual.reactive import reactive
from textual.widgets import Input, Label

class NameInput(Vertical):

    DEFAULT_CSS = """
    NameInput {
        height: auto;
    }
    """

    @dataclass
    class FirstChanged(Message):
        first_name: str

    @dataclass
    class LastChanged(Message):
        last_name: str

    def compose(self) -> ComposeResult:
        yield Input(placeholder="First name", id="first")
        yield Input(placeholder="Last name", id="last")

    @on(Input.Changed, "#first")
    def first_changing(self) -> None:
        self.post_message(self.FirstChanged(self.query_one("#first", Input).value))

    @on(Input.Changed, "#last")
    def last_changing(self) -> None:
        self.post_message(self.LastChanged(self.query_one("#last", Input).value))


class NameDisplay(Label):

    first: reactive[str] = reactive("")
    last: reactive[str] = reactive("")

    def refresh_name(self) -> None:
        self.update(f"{self.first} {self.last}")

    def _watch_first(self) -> None:
        self.refresh_name()

    def _watch_last(self) -> None:
        self.refresh_name()

class ExampleApp(App[None]):

    def compose(self) -> ComposeResult:
        yield NameInput()
        yield NameDisplay()

    def on_name_input_first_changed(self, event: NameInput.FirstChanged) -> None:
        self.query_one(NameDisplay).first = event.first_name

    def on_name_input_last_changed(self, event: NameInput.LastChanged) -> None:
        self.query_one(NameDisplay).last = event.last_name

if __name__ == "__main__":
    ExampleApp().run()

### name_input.py ends here
