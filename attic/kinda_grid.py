"""https://github.com/Textualize/textual/issues/3483"""

from textual import on
from textual.app import App, ComposeResult
from textual.containers import Grid
from textual.widgets import Label, Input, Log


class TitledInput(Grid):

    DEFAULT_CSS = """
    TitledInput {
        grid-size: 2;
        height: auto;
    }

    Label {
        background: green;
    }
    """

    def __init__(self, title: str) -> None:
        super().__init__()
        self.title = title

    def compose(self) -> ComposeResult:
        yield Label(self.title)
        yield Input()


class KindaGridApp(App[None]):

    def compose(self) -> ComposeResult:
        yield Log()
        for n in range(4):
            yield TitledInput(f"Input {n}")

    @on(Input.Changed)
    def update_logs(self, event: Input.Changed) -> None:
        self.query_one(Log).write_line(
            f"{event.control.parent.title} changed: {event.value}"
        )


if __name__ == "__main__":
    KindaGridApp().run()

### kinda_grid.py ends here
