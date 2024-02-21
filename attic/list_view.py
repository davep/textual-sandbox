"""https://github.com/Textualize/textual/discussions/1840"""

from textual.app import App, ComposeResult
from textual.widgets import ListView, ListItem, Label, Footer


class LabelItem(ListItem):

    def __init__(self, label: str) -> None:
        super().__init__()
        self.label = label

    def compose(self) -> ComposeResult:
        yield Label(self.label)


class ListViewExample(App):

    CSS_PATH = "list_view.css"

    def compose(self) -> ComposeResult:
        yield ListView(
            LabelItem("One"),
            LabelItem("Two"),
            LabelItem("Three"),
        )
        yield Label("Nothing chosen", id="chosen")
        yield Footer()

    def on_list_view_selected(self, event: ListView.Selected):
        self.query_one("#chosen", Label).update(event.item.label)


if __name__ == "__main__":
    app = ListViewExample()
    app.run()
