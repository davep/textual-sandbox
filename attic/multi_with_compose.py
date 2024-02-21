from textual.app import App, ComposeResult
from textual.containers import Vertical
from textual.widgets import Header, Footer, Label
from textual.binding import Binding


class MultiWithComposeApp(App[None]):

    CSS = """
    Vertical {
        border: solid red;
        align: center middle;
    }

    .hidden {
        display: none;
    }
    """

    BINDINGS = [
        Binding("h", "show_hide", "Show/Hide"),
    ]

    def compose(self) -> ComposeResult:
        yield Header()
        with Vertical(), Vertical(), Vertical(), Vertical(), Vertical(), Vertical(), Vertical(), Vertical(), Vertical(), Vertical(), Vertical(), Vertical(), Vertical(), Vertical(), Vertical(), Vertical(), Vertical(), Vertical(), Vertical(), Vertical():
            yield Label("Where does this go?")
        yield Footer()

    def action_show_hide(self) -> None:
        self.query_one("Screen > Vertical", Vertical).query(Vertical).toggle_class(
            "hidden"
        )


if __name__ == "__main__":
    MultiWithComposeApp().run()
