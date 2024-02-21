"""https://github.com/Textualize/textual/issues/4150"""

from __future__ import annotations

from textual import on
from textual.app import App, ComposeResult
from textual.containers import Vertical
from textual.widgets import TabbedContent, TabPane, Tabs, Tab, Label, Log, Rule


class TabbedContentActiveApp(App[None]):

    BINDINGS = [("c", "jump_tabbed_content"), ("t", "jump_tabs")]

    def compose(self) -> ComposeResult:
        with Vertical() as container:
            container.border_title = "TabbedContent version"
            with TabbedContent():
                for n in range(200):
                    with TabPane(f"Filler {n}", id=f"filler-{n}"):
                        yield Label(f"Filler tab {n}")
                with TabPane("PICK ME!", id="pick-me"):
                    yield Label("This is the tab we're after")
        with Vertical() as container:
            container.border_title = "Tabs version"
            yield Tabs(
                *(
                    tuple(Tab(f"Filler {n}", id=f"filler-{n}") for n in range(200))
                    + (Tab("PICK ME!", id="pick-me"),)
                )
            )
        yield Rule()
        yield Log()

    @on(TabbedContent.TabActivated)
    @on(Tabs.TabActivated)
    def log_messages(
        self, event: TabbedContent.TabActivated | Tabs.TabActivated
    ) -> None:
        self.query_one(Log).write_line(f"{event!r}")

    def action_jump_tabbed_content(self) -> None:
        self.query_one(TabbedContent).active = "pick-me"

    def action_jump_tabs(self) -> None:
        self.query_one("Vertical > Tabs", Tabs).active = "pick-me"


if __name__ == "__main__":
    TabbedContentActiveApp().run()

### tabbed_content_active.py ends here
