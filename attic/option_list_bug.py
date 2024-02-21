"""Test code for https://github.com/Textualize/textual/issues/3455"""

from textual.app import App, ComposeResult
from textual.widgets import OptionList, Log, Footer
from textual.widgets.option_list import Option


class OptionListAddBug(App[None]):

    BINDINGS = [(str(n), f"add({n})", f"Add {n}") for n in range(10)]

    CSS = """
    OptionList, Log {
        height: 1fr;
        border: round cornflowerblue;
    }
    """

    def compose(self) -> ComposeResult:
        yield OptionList()
        yield Log()
        yield Footer()

    def action_add(self, value: int) -> None:
        try:
            self.query_one(OptionList).add_option(
                Option(f"Added {value} just fine", id=f"id-{value}")
            )
        except Exception as error:
            self.query_one(Log).write_line(f"{error!r}")


if __name__ == "__main__":
    OptionListAddBug().run()

### option_list_bug.py ends here
