"""Auto-size TextArea with a max size."""

from textual.app import App, ComposeResult
from textual.containers import Vertical
from textual.widgets import TextArea


class MaxHeightEdit(App[None]):

    CSS = """
    Vertical {
        border: red;
        height: 50%;
    }

    TextArea {
        height: auto;
        min-height: 5;
        max-height: 1fr;
    }
    """

    def compose(self) -> ComposeResult:
        with Vertical():
            yield TextArea()


if __name__ == "__main__":
    MaxHeightEdit().run()

### max_edit.py ends here
