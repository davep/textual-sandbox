import asyncio

from textual.app import App, ComposeResult
from textual.containers import Vertical
from textual.widgets import DataTable, Label, LoadingIndicator
from textual import work

class BackgroundLoad(App[None]):

    CSS = """
    DataTable {
        height: 100%;
    }

    .hidden {
        display: none;
    }
    """

    def compose(self) -> ComposeResult:
        with Vertical(id="loader"):
            yield Label("Just a moment while I load up the data...")
            yield LoadingIndicator()
        yield DataTable(classes="hidden")

    def on_mount(self):
        self.query_one(DataTable).add_column("Column")
        self.load_data()

    @work
    async def load_data(self):
        t = self.query_one(DataTable)
        for i in range(500):
            t.add_row(i, key=str(i))
            await asyncio.sleep(0.01)
        t.set_class(False, "hidden")
        self.query_one("#loader", Vertical).set_class(True,"hidden")
        self.call_after_refresh(t.action_scroll_end)

if __name__ == "__main__":
    BackgroundLoad().run()
