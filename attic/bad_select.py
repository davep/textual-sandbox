"""https://github.com/Textualize/textual/pull/3614"""

from textual import on
from textual.app import App, ComposeResult
from textual.widgets import Button, Label, Select


class BadSelectApp(App[None]):

    def compose(self) -> ComposeResult:
        yield Select[int](
            (
                ("Filthy", 0),
                ("Rich", 1),
                ("Catflap", 2),
            ),
            allow_blank=False,
            value=1,
        )
        yield Label()
        yield Button("Make bad")

    @on(Select.Changed)
    def show_value(self) -> None:
        self.query_one(Label).update(f"{self.query_one(Select).value!r}")

    @on(Button.Pressed)
    def make_bad(self) -> None:
        self.query_one(Select).value = "nope"
        self.show_value()


if __name__ == "__main__":
    BadSelectApp().run()

### bad_select.py ends here
