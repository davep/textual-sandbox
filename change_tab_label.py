"""Example of changing a TabPane label."""

from textual.app import App, ComposeResult
from textual.widgets import TabbedContent, TabPane


class ChangeTabLabelApp(App[None]):
    def compose(self) -> ComposeResult:
        with TabbedContent():
            yield TabPane("Initial", id="change-me")

    def on_mount(self) -> None:
        self.query_one(TabbedContent).get_tab("change-me").label = "Changed!"


if __name__ == "__main__":
    ChangeTabLabelApp().run()

### change_tab_label.py ends here
