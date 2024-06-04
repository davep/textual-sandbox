"""Sorting ListItems based on classes.

For a question in Discord.
"""

from textual.app import App, ComposeResult
from textual.widgets import Label, ListItem, ListView


class SortedListView(App[None]):
    def compose(self) -> ComposeResult:
        yield ListView(
            ListItem(Label("Bottom")),
            ListItem(Label("Top"), classes="top"),
            ListItem(Label("Bottom")),
            ListItem(Label("Top"), classes="top"),
            ListItem(Label("Bottom")),
            ListItem(Label("Top"), classes="top"),
            ListItem(Label("Bottom")),
            ListItem(Label("Top"), classes="top"),
            ListItem(Label("Bottom")),
            ListItem(Label("Top"), classes="top"),
            ListItem(Label("Bottom")),
            ListItem(Label("Top"), classes="top"),
        )

    def on_mount(self) -> None:
        self.query_one(ListView).sort_children(key=lambda item: item.has_class("top"))


if __name__ == "__main__":
    SortedListView().run()

### sorted_listview.py ends here
