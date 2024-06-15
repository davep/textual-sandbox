"""Setting tooltips on tabs."""

from textual.app import App, ComposeResult
from textual.widgets import TabbedContent, TabPane


class TabTooltipsApp(App[None]):
    def compose(self) -> ComposeResult:
        with TabbedContent():
            yield TabPane("First", id="first")
            yield TabPane("Second", id="second")
            yield TabPane("Third", id="third")

    def on_mount(self) -> None:
        tabs = self.query_one(TabbedContent)
        tabs.get_tab("first").tooltip = "Hey look it's the first tab!"
        tabs.get_tab("second").tooltip = "I'm the second!"
        tabs.get_tab("third").tooltip = "Me? I'm the third tab of course!"


if __name__ == "__main__":
    TabTooltipsApp().run()

### tab_tooltips.py ends here
