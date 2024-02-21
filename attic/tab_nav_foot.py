"""https://github.com/Textualize/textual/discussions/3620"""

from dataclasses import replace

from textual.app import App, ComposeResult
from textual.widgets import TabbedContent, TabPane, Footer, Label, Tabs


class TabNavFooterApp(App[None]):

    def compose(self) -> ComposeResult:
        with TabbedContent():
            with TabPane("One"):
                yield Label("One")
            with TabPane("Two"):
                yield Label("Two")
        yield Footer()

    def on_mount(self) -> None:
        tab_keys = self.query_one(Tabs)._bindings.keys
        tab_keys["left"] = replace(tab_keys["left"], show=True)
        tab_keys["right"] = replace(tab_keys["right"], show=True)


if __name__ == "__main__":
    TabNavFooterApp().run()

### tab_nav_foot.py ends here
