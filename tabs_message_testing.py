"""Tabs testing for https://github.com/Textualize/textual/issues/3869"""

from textual import on
from textual.app import App, ComposeResult
from textual.containers import Container, Horizontal
from textual.message import Message
from textual.widgets import Button, Log, Tabs


class WrapperForTesting(Container):
    DEFAULT_CSS = """
    WrapperForTesting {
        Horizontal, Tabs {
            height: auto;
        }
    }
    """

    def compose(self) -> ComposeResult:
        with Horizontal():
            yield Button("Select 3", id="select")
            yield Button("Disable 3", id="disable")
            yield Button("Enable 3", id="enable")
            yield Button("Hide 3", id="hide")
            yield Button("Show 3", id="show")
            yield Button("Clear", id="clear")
            yield Button("Empty active", id="empty-active")
            yield Button("Hide all", id="hide-all")
        yield Tabs("One", "Two", "Three", "Four", "Five")

    @on(Button.Pressed, "#select")
    def select_tab(self) -> None:
        self.query_one(Tabs).active = "tab-3"

    @on(Button.Pressed, "#disable")
    def disable_tab(self) -> None:
        self.query_one(Tabs).disable("tab-3")

    @on(Button.Pressed, "#enable")
    def enable_tab(self) -> None:
        self.query_one(Tabs).enable("tab-3")

    @on(Button.Pressed, "#hide")
    def hide_tab(self) -> None:
        self.query_one(Tabs).hide("tab-3")

    @on(Button.Pressed, "#show")
    def show_tab(self) -> None:
        self.query_one(Tabs).show("tab-3")

    @on(Button.Pressed, "#clear")
    def clear_tabs(self) -> None:
        self.query_one(Tabs).clear()

    @on(Button.Pressed, "#empty-active")
    def empty_active(self) -> None:
        self.query_one(Tabs).active = ""

    @on(Button.Pressed, "#hide-all")
    def hide_all(self) -> None:
        for n in range(5):
            self.query_one(Tabs).hide(f"tab-{n+1}")


class TabsMessagesTestingApp(App[None]):
    def compose(self) -> ComposeResult:
        yield WrapperForTesting()
        yield Log()

    @on(Tabs.TabActivated)
    @on(Tabs.TabDisabled)
    @on(Tabs.TabEnabled)
    @on(Tabs.TabHidden)
    @on(Tabs.TabShown)
    @on(Tabs.Cleared)
    def log_message(self, event: Message):
        self.query_one(Log).write_line(f"{event!r}")


if __name__ == "__main__":
    TabsMessagesTestingApp().run()

### tabs_message_testing.py ends here
