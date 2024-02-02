"""Example of aligning a label, for Discord."""

from textual.app import App, ComposeResult
from textual.containers import Horizontal
from textual.widgets import Button, Label, Input

class AlignLabelApp(App[None]):

    CSS = """
    #fire-command {
        height: 3;

        Input {
            width: 1fr;
        }

        Label {
            height: 1fr;
            content-align: center middle;
        }
    }
    """

    def compose(self) -> ComposeResult:
        with Horizontal(id="fire-command"):
            yield Label("Target coordinates:")
            yield Input(placeholder="It's the only way to be sure")
            yield Button("Nuke From Orbit")

if __name__ == "__main__":
    AlignLabelApp().run()

### align_label.py ends here
