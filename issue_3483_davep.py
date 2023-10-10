"""https://github.com/Textualize/textual/issues/3483"""

from textual.app import App, ComposeResult
from textual.containers import Grid
from textual.widgets import Label, Input, Select

class StandardRow(Grid):
    """A standard row in the display.

    Other compound widgets inherit from this.
    """

    DEFAULT_CSS = """
    StandardRow {
        grid-size: 3;
        grid-columns: 12 1fr 1fr;
        height: auto;
        margin-bottom: 1;
    }
    """

class InputWithLabel(StandardRow):
    """A labeled input row with optional select."""

    def __init__(self, input_label: str, with_select: bool = False) -> None:
        self.input_label = input_label
        self.with_select = with_select
        super().__init__()

    def compose(self) -> ComposeResult:
        yield Label(self.input_label)
        yield Input()
        if self.with_select:
            yield Select([("a", "A"), ("b", "B"), ("c", "C")])

class Issue3483Example(App[None]):

    def compose(self) -> ComposeResult:
        yield InputWithLabel("First Name")
        yield InputWithLabel("Last Name", with_select=True)
        yield InputWithLabel("Email")

if __name__ == "__main__":
    Issue3483Example().run()

### issue_3483_davep.py ends here
