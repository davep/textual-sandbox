from textual.app import App, ComposeResult
from textual.containers import Horizontal, Vertical
from textual.widgets import Header, Footer, Label
from textual.binding import Binding
from textual.reactive import reactive


class LotsacolumnsApp(App[None]):

    CSS = """
    Vertical {
        border: round red;
        width: 1fr;
    }
    """

    BINDINGS = [
        Binding("n", "new", "New Column"),
    ]

    col = reactive(0)

    def compose(self) -> ComposeResult:
        yield Header()
        yield Horizontal()
        yield Footer()

    def action_new(self) -> None:
        """"""
        self.query_one(Horizontal).mount(Vertical(Label(str(self.col))))
        self.col += 1


if __name__ == "__main__":
    LotsacolumnsApp().run()
