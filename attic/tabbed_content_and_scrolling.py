from textual.app import App, ComposeResult
from textual.containers import VerticalScroll
from textual.widgets import TabbedContent, Input, LoadingIndicator, TabPane, Markdown


class TabPaneScrollableContent(VerticalScroll, can_focus=False):
    pass


class TabbedContentWithScrollApp(App[None]):

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

    Markdown {
        margin: 0;
    }

    Input {
        border: wide $background;
        padding: 1 2;
    }

    Input:focus {
        border: wide $accent;
    }

    TabPaneScrollableContent > * {
        margin-right: 2;
    }
    """

    def compose(self) -> ComposeResult:
        with TabbedContent():
            with TabPane("Loading!", classes="center-things"):
                yield LoadingIndicator()
            with TabPane("Enter lots of things"):
                with TabPaneScrollableContent():
                    for n in range(50):
                        yield Markdown(f"# Here is some markdown before input {n}!")
                        yield Input(placeholder=f"This is input {n}")


if __name__ == "__main__":
    TabbedContentWithScrollApp().run()
