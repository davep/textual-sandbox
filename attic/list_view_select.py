"""Example of handling ListView.Selected for a question on Discord."""

from textual import on
from textual.app import App, ComposeResult
from textual.widgets import ListView, ListItem, Label


class ListViewMessageExampleApp(App[None]):

    def compose(self) -> ComposeResult:
        yield Label("Chosen item will appear here", id="chosen")
        yield ListView(
            ListItem(Label("Mal"), id="mal"),
            ListItem(Label("Zoe"), id="zoe"),
            ListItem(Label("Wash"), id="wash"),
            ListItem(Label("Jayne"), id="jayne"),
            ListItem(Label("Book"), id="book"),
            ListItem(Label("Simon"), id="simon"),
            ListItem(Label("River"), id="river"),
        )

    @on(ListView.Selected)
    def show_chosen(self, event: ListView.Selected) -> None:
        self.query_one("#chosen", Label).update(f"{event.item}")


if __name__ == "__main__":
    ListViewMessageExampleApp().run()

### list_view_select.py ends here
