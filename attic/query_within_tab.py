from textual.app import App, ComposeResult
from textual.widgets import TabbedContent, TabPane, Button


class QueryWithinTabPane(App[None]):

    def compose(self) -> ComposeResult:
        with TabbedContent():
            with TabPane("First", id="first"):
                yield Button("On first")
            with TabPane("Second", id="second"):
                yield Button("On second")
            with TabPane("Third", id="third"):
                yield Button("On third")

    def on_mount(self) -> None:
        self.query_one(
            f"TabPane#{self.query_one(TabbedContent).active} Button", Button
        ).label = "I found and modified this"


if __name__ == "__main__":
    QueryWithinTabPane().run()
