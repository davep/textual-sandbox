"""https://github.com/Textualize/textual/issues/1565"""

from textual.app import App, ComposeResult, RenderResult
from textual.widgets import Header, Footer, Label
from textual.reactive import reactive


class MyLabel(Label, can_focus=True):

    BINDINGS = [("up", "move(1)", "Up"), ("down", "move(-1)", "Down")]

    counter = reactive(0)

    def render(self) -> RenderResult:
        """Render the content of the widget."""
        return f"{self.counter=}"

    def action_move(self, direction: int) -> None:
        self.counter += direction


class Issue1565App(App[None]):

    BINDINGS = [
        ("s", "show", "Show"),
        ("h", "hide", "Hide"),
    ]

    CSS = """
    Screen {
        align: center middle;
    }

    MyLabel {
        text-align: center;
    }

    MyLabel.hidden {
        display: none;
    }

    MyLabel:focus {
        border: round $primary;
    }
    """

    def compose(self) -> ComposeResult:
        yield Header()
        yield MyLabel()
        yield Footer()

    def on_mount(self) -> None:
        self.query_one(MyLabel).focus()

    def action_show(self) -> None:
        self.query_one(MyLabel).set_class(False, "hidden")

    def action_hide(self) -> None:
        self.query_one(MyLabel).set_class(True, "hidden")


if __name__ == "__main__":
    Issue1565App().run()
