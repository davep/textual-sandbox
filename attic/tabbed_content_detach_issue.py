"""https://github.com/Textualize/textual/issues/2229"""

from textual.app import App, ComposeResult
from textual.binding import Binding
from textual.containers import Vertical
from textual.widgets import Header, Footer, TabbedContent, TabPane, Tabs, DirectoryTree


class SelfFocusPane(TabPane):

    DEFAULT_CSS = """
    SelfFocusPane {
        height: 100% !important;
    }
    DirectoryTree {
        width: 100%;
        height: 100% !important;
    }
    """

    def compose(self) -> ComposeResult:
        """Compose the child widgets."""
        yield DirectoryTree(".")

    def on_show(self) -> None:
        self.query_one(DirectoryTree).focus()


class TabbedContentIssueApp(App[None]):

    CSS = """
    Screen {
        align: center middle;
    }

    Screen > Vertical {
        width: 42;
    }

    TabbedContent {
        border: round red;
        max-width: 40;
        height: 100%;
    }

    ContentSwitcher {
        height: 1fr !important;
    }
    """

    BINDINGS = [
        Binding("shift+left", "previous", "Previous"),
        Binding("shift+right", "next", "Next"),
    ]

    def compose(self) -> ComposeResult:
        yield Header()
        with Vertical():
            with TabbedContent():
                for n in range(6):
                    yield SelfFocusPane(f"Tab {n}")
        yield Footer()

    def on_mount(self) -> None:
        self.query_one(Tabs).focus()

    def action_previous(self) -> None:
        self.query_one(Tabs).action_previous_tab()

    def action_next(self) -> None:
        self.query_one(Tabs).action_next_tab()


if __name__ == "__main__":
    TabbedContentIssueApp().run()
