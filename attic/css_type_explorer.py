"""https://github.com/Textualize/textual/pull/2753"""

from textual.app import App, ComposeResult, RenderResult
from textual.containers import Horizontal, Vertical
from textual.widgets import Static, TextLog


class CustomParent(Static):

    def __init__(self) -> None:
        super().__init__()
        self.border_title = self.__class__.__name__

    def render(self) -> RenderResult:
        return str(self._css_type_names)


class CustomChild(CustomParent):
    pass


class CustomGrandChild(CustomChild, inherit_css=False):
    pass


class CSSTypeExplorerApp(App[None]):

    CSS = """
    Static, TextLog {
        border: panel green;
        padding: 1;
    }

    CustomGrandChild {
        border: panel red;
    }
    """

    def compose(self) -> ComposeResult:
        with Horizontal():
            with Vertical():
                yield CustomParent()
                yield CustomChild()
                yield CustomGrandChild()
            with Vertical():
                yield TextLog(id="statics")
                yield TextLog(id="query-one")

    def on_mount(self) -> None:
        self.query_one("#statics", TextLog).border_title = "Statics in the DOM"
        for static in self.query(Static):
            self.query_one("#statics", TextLog).write(f"{static!r}")
        self.query_one("#query-one", TextLog).border_title = (
            "query_one( 'CustomChild' )"
        )
        self.query_one("#query-one", TextLog).write(
            f"{self.query_one( CustomChild )!r}"
        )


if __name__ == "__main__":
    CSSTypeExplorerApp().run()
