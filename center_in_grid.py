"""Example of centring a widget in a span in a grid.

For a question in Discord.
"""

from textual.app import App, ComposeResult
from textual.containers import Center, Grid
from textual.widgets import Button


class CenterGridSpanApp(App[None]):
    CSS = """
    Grid {
        grid-size: 3 3;
    }

    #big {
        column-span: 3;
        Button {
            height: 1fr;
        }
    }
    """

    def compose(self) -> ComposeResult:
        with Grid():
            with Center(id="big"):
                yield Button("Big Bada Button!")
            for _ in range(6):
                yield Button("Smol Button!")


if __name__ == "__main__":
    CenterGridSpanApp().run()

### center_in_grid.py ends here
