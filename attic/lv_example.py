from textual.app import App, ComposeResult
from textual.widgets import Header, Footer, ListView, ListItem, Label


class Choices(ListView):

    def __init__(self, choices: list[str]) -> None:
        super().__init__()
        self._choices = choices

    def compose(self) -> ComposeResult:
        """Compose the child widgets."""
        for choice in self._choices:
            yield ListItem(Label(choice))


class ListViewExample(App[None]):

    CSS = """
    Screen {
        align: center middle;
    }

    Choices {
        border: round blue;
        width: 50%;
        height: 10;
    }
    """

    def compose(self) -> ComposeResult:
        yield Header()
        yield Choices(["One", "Two", "Three", "More"])
        yield Label("Nothing selected right now", id="chosen")
        yield Footer()

    def on_list_view_selected(self, event: ListView.Selected) -> None:
        self.query_one("#chosen", Label).update(
            f"Selected: {event.item.children[ 0 ].renderable}"
        )


if __name__ == "__main__":
    ListViewExample().run()
