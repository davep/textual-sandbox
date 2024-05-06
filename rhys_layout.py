"""Layout example for a question on Discord."""

from textual.app import App, ComposeResult
from textual.containers import Horizontal, Vertical
from textual.widgets import Static


class RhysLayoutApp(App[None]):
    CSS = """
    Static {
        background: white;
        border: round black;
        color: black;
        width: 1fr;
        height: 1fr;
    }

    #interfaces, #command-line {
        height: 7;
    }

    .that-certain-command-mode {
        display: none;
    }
    """

    BINDINGS = [
        ("space", "toggle_certain_command"),
    ]

    def compose(self) -> ComposeResult:
        with Horizontal():
            with Vertical():
                yield Static("Interfaces", id="interfaces")
                yield Static("Command Line", id="command-line")
                yield Static("Output", id="output")
            with Vertical():
                yield Static("Whatever goes here")

    def action_toggle_certain_command(self) -> None:
        self.query_one("#interfaces").toggle_class("that-certain-command-mode")


if __name__ == "__main__":
    RhysLayoutApp().run()

### rhys_layout.py ends here
