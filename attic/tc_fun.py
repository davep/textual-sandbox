"""https://github.com/Textualize/textual/issues/3695"""

from textual.app import App, ComposeResult
from textual.containers import Horizontal
from textual.widgets import TabbedContent, TabPane, Label, Static


class TabContentFun(App[None]):

    CSS = """
    ContentTab#first {
        color: red;
    }

    ContentTab#second {
        color: green;
    }

    TabbedContent, #tree {
        width: 1fr;
    }
    """

    def compose(self) -> ComposeResult:
        with Horizontal():
            with TabbedContent():
                with TabPane("First", id="first"):
                    yield Label("First")
                with TabPane("Second", id="second"):
                    yield Label("Second")
            yield Static(id="tree")

    def on_mount(self) -> None:
        self.query_one("#tree", Static).update(self.query_one(TabbedContent).tree)


if __name__ == "__main__":
    TabContentFun().run()

### tc_fun.py ends here
