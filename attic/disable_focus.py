from textual.app import App, ComposeResult
from textual.containers import Vertical
from textual.widgets import Input


class DisableFocus(App[None]):

    BINDINGS = [
        ("ctrl+z", "disable"),
    ]

    def compose(self) -> ComposeResult:
        with Vertical():
            yield Input()

    def action_disable(self) -> None:
        self.query_one(Vertical).disabled = not self.query_one(Vertical).disabled


if __name__ == "__main__":
    DisableFocus().run()
