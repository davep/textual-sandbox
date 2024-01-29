"""For a question on Discord."""

from textual import on
from textual.app import App, ComposeResult
from textual.widgets import ListView, ListItem, Label

class URLItem(ListItem):

    def __init__(self, title: str, url: str) -> None:
        super().__init__()
        self.title = title
        self.url = url

    def compose(self) -> ComposeResult:
        yield Label(self.title)


class ListViewExampleApp(App[None]):

    def compose(self) -> ComposeResult:
        yield Label("Chosen will go here", id="result")
        yield ListView(
            URLItem("Textual", "https://textual.textualize.io/"),
            URLItem("Rich", "https://rich.readthedocs.io/en/stable/introduction.html"),
            URLItem("Textualize", "https://textualize.io/"),
        )

    @on(ListView.Selected)
    def url_choice(self, event: ListView.Selected) -> None:
        assert isinstance(event.item, URLItem)
        self.query_one("#result", Label).update(event.item.url)

if __name__ == "__main__":
    ListViewExampleApp().run()

### list_view_urls.py ends here
