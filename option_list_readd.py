"""Test code for https://github.com/Textualize/textual/issues/4101"""

from textual import on
from textual.app import App, ComposeResult
from textual.containers import Horizontal
from textual.reactive import var
from textual.widgets import Button, OptionList, Pretty
from textual.widgets.option_list import Option


class OptionListReAdd(App[None]):

    CSS = """
    OptionList {
        height: 1fr;
    }

    Horizontal {
        height: 2fr;
        Pretty {
            width: 1fr;
        }
    }
    """

    count: var[int] = var(0)

    def compose(self) -> ComposeResult:
        yield Button("Add again")
        yield OptionList()
        with Horizontal():
            yield Pretty([], id="options")
            yield Pretty([], id="ids")

    @on(Button.Pressed)
    def readd(self) -> None:
        self.count += 1
        self.query_one(OptionList).add_option(
            Option(f"Option {self.count}", id=str(self.count))
        )
        self.query_one("#options", Pretty).update(self.query_one(OptionList)._options)
        self.query_one("#ids", Pretty).update(self.query_one(OptionList)._option_ids)


if __name__ == "__main__":
    OptionListReAdd().run()

### option_list_readd.py ends here
