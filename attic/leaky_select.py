"""Example for https://github.com/Textualize/textual/issues/4224"""

from textual import on
from textual.app import App, ComposeResult
from textual.widgets import Log, OptionList, Select


class LeakySelectApp(App[None]):
    def compose(self) -> ComposeResult:
        yield Log()
        yield OptionList(*(f"This is option {n}" for n in range(10)))
        yield Select[int](((f"This is selection {n}", n) for n in range(10)))

    @on(OptionList.OptionHighlighted)
    def log_some_option(self, event: OptionList.OptionHighlighted) -> None:
        self.query_one(Log).write_line(f"{event}")


if __name__ == "__main__":
    LeakySelectApp().run()

### leaky_select.py ends here
