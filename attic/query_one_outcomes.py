from textual.app import App, ComposeResult
from textual.containers import Vertical
from textual.widgets import Header, Footer, Button, Static, Label


class QueryOneOutcomesApp(App[None]):

    CSS = """
    Vertical {
        align: center middle;
    }

    Label {
        width: auto;
    }

    .hidden {
        display: none;
    }
    """

    def compose(self) -> ComposeResult:
        yield Header()
        yield Vertical(
            Button("Find nothing", id="find-nothing"),
            Button("Find one", id="find-one"),
            Button("Find many", id="find-many"),
            Label("Outcome will appear here"),
            *[Static(id=f"static-{n}", classes="hidden") for n in range(10)],
        )
        yield Footer()

    def on_button_pressed(self, event: Button.Pressed) -> None:
        try:
            if event.button.id == "find-nothing":
                found = self.query_one("#the-treachery-of-widgets", Static)
            elif event.button.id == "find-one":
                found = self.query_one("#static-3", Static)
            elif event.button.id == "find-many":
                found = self.query_one(Static)
            else:
                found = "Ceci n'est pas une button!"
        except Exception as err:
            found = f"Exception: {type( err ).__name__}"
        self.query_one(Label).update(str(found))


if __name__ == "__main__":
    QueryOneOutcomesApp().run()
