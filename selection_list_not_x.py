"""Tweaking the SelectionList button inner.

For a question on Discord.
"""

from textual.app import App, ComposeResult
from textual.widgets import SelectionList
from textual.widgets._toggle_button import ToggleButton

ToggleButton.BUTTON_INNER = "O"


class SelctionListCharApp(App[None]):
    def compose(self) -> ComposeResult:
        yield SelectionList[int](*((f"Selection {n}", n) for n in range(20)))


if __name__ == "__main__":
    SelctionListCharApp().run()

### selection_list_not_x.py ends here
