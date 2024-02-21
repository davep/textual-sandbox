from textual.app import App, ComposeResult
from textual.widgets import TabbedContent, TabPane, LoadingIndicator


class LoadingInTabPaneApp(App[None]):

    CSS = """
    TabbedContent ContentSwitcher {
        height: 1fr;
    }

    ContentSwitcher .center-things {
        align: center middle;
        height: 1fr;
    }

    LoadingIndicator {
        height: auto;
    }
    """

    def compose(self) -> ComposeResult:
        with TabbedContent():
            with TabPane("Loading!", classes="center-things"):
                yield LoadingIndicator()


if __name__ == "__main__":
    LoadingInTabPaneApp().run()
