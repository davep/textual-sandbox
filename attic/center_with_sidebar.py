"""https://github.com/Textualize/textual/discussions/1557"""

from textual.app import App, ComposeResult
from textual.containers import Vertical
from textual.widgets import Header, Footer, Button


class SidebarExample(App[None]):

    CSS = """
    Screen {
        layers: base sidebar;
    }

    #base {
        align: center middle;
        layer: base;
    }

    #sidebar {
        layer: sidebar;
        border: round red;
        height: auto;
        width: auto;
    }
    """

    def compose(self) -> ComposeResult:
        yield Header()
        yield Vertical(
            Button("Test Button "),
            Button("Test Button "),
            Button("Test Button "),
            Button("Test Button "),
            Button("Test Button "),
            id="base",
        )
        yield Vertical(
            Button("Side Button"),
            Button("Side Button"),
            Button("Side Button"),
            id="sidebar",
        )
        yield Footer()


if __name__ == "__main__":
    SidebarExample().run()
