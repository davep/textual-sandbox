"""https://discord.com/channels/1026214085173461072/1033754296224841768/1139134772287905802"""

from textual.app import App, ComposeResult
from textual.widgets import TabbedContent, TabPane


class SelectTabbedContent(App[None]):

    def compose(self) -> ComposeResult:
        with TabbedContent():
            yield TabPane("Hello", id="hello")

    def on_mount(self) -> None:
        _ = self.query_one("TabPane#hello", TabPane)


if __name__ == "__main__":
    SelectTabbedContent().run()
