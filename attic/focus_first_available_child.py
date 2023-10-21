"""Example of focusing first available child, for Discord."""

from textual.app import App, ComposeResult
from textual.containers import Horizontal, Vertical
from textual.widget import Widget
from textual.widgets import Label, Input, Button
from textual.walk import walk_depth_first

def focus_first_child(widget: Widget) -> None:
    """Focus the first focusable child of the given widget.

    Args:
        widget: The widget to place focus within.
    """
    for child in walk_depth_first(widget, Widget):
        if child.can_focus:
            child.focus()
            break

class FocusFirstAvailableChildApp(App[None]):

    CSS = """
    Vertical {
        border: round cornflowerblue;
    }
    """

    def compose(self) -> ComposeResult:
        with Horizontal():
            with Vertical(id="not-in-here"):
                yield Label("This can't get focus")
                yield Button("But this can")
                yield Input(placeholder="And so can this")
            with Vertical(id="in-here"):
                yield Label("This can't get focus")
                yield Button("But this can")
                yield Input(placeholder="And so can this")

    def on_mount(self) -> None:
        focus_first_child(self.query_one("#in-here"))

if __name__ == "__main__":
    FocusFirstAvailableChildApp().run()

### focus_first_available_child.py ends here
