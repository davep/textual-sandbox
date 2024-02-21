from textual.app import App, ComposeResult
from textual.widgets import Label, Header, Footer
from textual.containers import Vertical
from textual.binding import Binding


class BorkFooter(App[None]):

    TITLE = "Footer Borker"

    BINDINGS = [
        Binding("a", "a", "The A key"),
        Binding("backspace", "backspace", "Backspace!"),
        Binding("delete", "delete", "Delete!"),
    ]

    def compose(self) -> ComposeResult:
        yield Header()
        yield Vertical()
        yield Footer()

    def gndn(self):
        self.query_one(Vertical).mount(Label("You pressed a key"))

    def action_a(self):
        self.gndn()

    def action_backspace(self):
        self.gndn()

    def action_delete(self):
        self.gndn()


if __name__ == "__main__":
    BorkFooter().run()
