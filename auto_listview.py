"""Auto-generated ListView message example.

For a question on Discord.
"""

from textual import on
from textual.app import App, ComposeResult
from textual.widgets import Label, ListItem, ListView


class AutoListViewApp(App[None]):
    def compose(self) -> ComposeResult:
        yield ListView(ListItem(Label("Pick me!"), id="pick-me"))

    @on(ListView.Selected)
    def picked(self, event: ListView.Selected) -> None:
        self.notify(f"I got the {event!r} event")

    def on_mount(self) -> None:
        list_view = self.query_one(ListView)
        list_item = list_view.query_one("#pick-me", ListItem)
        list_view.post_message(ListView.Selected(list_view, list_item))


if __name__ == "__main__":
    AutoListViewApp().run()

### auto_listview.py ends here
