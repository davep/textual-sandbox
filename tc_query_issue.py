"""For https://github.com/Textualize/textual/issues/3695"""

from textual import on
from textual.app import App, ComposeResult
from textual.containers import Horizontal
from textual.widgets import Button, TabbedContent, TabPane, Label, Log, Static

class TabbedDiscontentApp(App[None]):

    CSS = """
    #info > * {
        width: 1fr;
    }
    """

    def compose(self) -> ComposeResult:
        with TabbedContent():
            for n in range(10):
                with TabPane(f"Tab {n}", id=f"test-{n}"):
                    yield Label(f"Hello from test pane {n}")
        yield Button("Query TabPane 1")
        with Horizontal(id="info"):
            yield Static(id="dom")
            yield Log()

    def on_mount(self) -> None:
        self.query_one("#dom", Static).update(
            self.query_one(TabbedContent).tree
        )

    @on(Button.Pressed)
    def test_it(self) -> None:
        self.notify(
            f"{self.query_one('#test-1')!r}"
        )
        self.query_one(TabbedContent).active = "test-1"

    @on(TabbedContent.TabActivated)
    def logger(self, event: TabbedContent.TabActivated) -> None:
        self.query_one(Log).write_line(f"{event!r}")
        self.query_one(Log).write_line(f"Active is '{self.query_one(TabbedContent).active}'")

if __name__ == "__main__":
    TabbedDiscontentApp().run()

### tc_query_issue.py ends here
