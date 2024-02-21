"""https://github.com/Textualize/textual/discussions/3559"""

from textual.app import App, ComposeResult
from textual.widgets import SelectionList
from textual.widgets.selection_list import Selection


class SelectionListError(App[None]):

    def compose(self) -> ComposeResult:
        yield SelectionList[str](Selection("Test", "test", id="test"))

    def on_mount(self) -> None:
        self.query_one(SelectionList).remove_option("test")


if __name__ == "__main__":
    SelectionListError().run()

### selection_list_error.py ends here
