"""For https://github.com/Textualize/textual/issues/3695"""

from textual import on
from textual.app import App, ComposeResult
from textual.widgets import Button, TabbedContent, TabPane, Label

class TabbedDiscontentApp(App[None]):

    def compose(self) -> ComposeResult:
        with TabbedContent():
            for n in range(10):
                with TabPane(f"Tab {n}", id=f"test-{n}"):
                    yield Label(f"Hello from test pane {n}")
        yield Button("Query TabPane 1")

    @on(Button.Pressed)
    def test_it(self) -> None:
        self.notify(
            f"{self.query_one('#test-1')!r}"
        )

if __name__ == "__main__":
    TabbedDiscontentApp().run()

### tc_query_issue.py ends here
