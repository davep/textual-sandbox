"""Example for a question on Discord."""

from rich.text import Text

from textual.app import App, ComposeResult, RenderResult
from textual.reactive import reactive
from textual.containers import Vertical, VerticalScroll
from textual.widget import Widget
from textual.widgets import Input


class TextDisplayWidget(Widget):

    DEFAULT_CSS = """
    TextDisplayWidget {
        height: auto;
    }
    """

    line_count: reactive[int] = reactive(500, layout=True)
    line_prefix: reactive[str] = reactive("This is an example")

    def render(self) -> RenderResult:
        return Text(
            "\n".join(f"{self.line_prefix} {n}" for n in range(self.line_count))
        )


class ScrollTextThingApp(App[None]):

    CSS = """
    Screen {
        layout: horizontal;
    }

    #display, #controls {
        width: 1fr;
    }
    """

    BINDINGS = [
        ("1", "lines(1)"),
        ("2", "lines(2)"),
        ("3", "lines(3)"),
        ("4", "lines(4)"),
        ("5", "lines(5)"),
        ("6", "lines(6)"),
        ("7", "lines(7)"),
        ("8", "lines(8)"),
        ("9", "lines(9)"),
        ("f1", "text('Hey, you pressed F1!')"),
        ("f2", "text('So this reactive thing is kinda cool right?')"),
    ]

    def compose(self) -> ComposeResult:
        with VerticalScroll(id="display"):
            yield TextDisplayWidget()
        with Vertical(id="controls"):
            for n in range(10):
                yield Input(placeholder=f"This is input {n}")

    def action_lines(self, lines: int) -> None:
        self.query_one(TextDisplayWidget).line_count = 10 * lines

    def action_text(self, text: str) -> None:
        self.query_one(TextDisplayWidget).line_prefix = text


if __name__ == "__main__":
    ScrollTextThingApp().run()

### scroll_thing.py ends here
