"""https://github.com/Textualize/textual/issues/3695"""

from textual.app import App, ComposeResult
from textual.widgets import TabbedContent, TabPane, Label

class TabContentFun(App[None]):

    CSS = """
    ContentTab#first {
        color: red;
    }

    ContentTab#second {
        color: green;
    }
    """

    def compose(self) -> ComposeResult:
        with TabbedContent():
            with TabPane("First", id="first"):
                yield Label("First")
            with TabPane("Second", id="second"):
                yield Label("second")

if __name__ == "__main__":
    TabContentFun().run()

### tc_fun.py ends here
