from textual.app import App, ComposeResult
from textual.geometry import Offset
from textual.widgets import Static
from textual.containers import Container


class Demo(App):

    TITLE = "Demonstration"

    BINDINGS = [
        ("b", "toggle_sidebar", "Sidebar"),
    ]

    CSS = """
    #sidebar {
        width: 40;
        background: $panel;
    }
    """

    def compose(self) -> ComposeResult:
        self.bar = Container(Static("Textual Demo"), id="sidebar")
        yield self.bar

    def action_toggle_sidebar(self) -> None:
        self.bar.styles.animate("offset", value=Offset(0, 0), duration=2.5)


if __name__ == "__main__":
    Demo().run()
