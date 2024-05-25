"""Handling a Tabs event.

For a question on Discord.
"""

from textual import on
from textual.app import App, ComposeResult
from textual.widgets import Tabs


class TabsEventsApp(App[None]):
    def compose(self) -> ComposeResult:
        yield Tabs(
            "Mal", "Zoë", "Wash", "Inara", "Jayne", "Kaylee", "Simon", "River", "Book"
        )

    @on(Tabs.TabActivated)
    def tab_activated(self, event: Tabs.TabActivated) -> None:
        self.notify(str(event.tab.label))


if __name__ == "__main__":
    TabsEventsApp().run()

### tabs_events.py ends here
