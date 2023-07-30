from textual.app import App, ComposeResult
from textual.containers import Horizontal, Vertical
from textual.widgets import DataTable

class SingleRowTableApp(App[None]):

    CSS = """
    Vertical {
        border: solid cornflowerblue;
        height: 5;
    }

    DataTable.fix-height {
        height: 1fr;
    }
    """

    def populate(self, table: DataTable ) -> DataTable:
        table.add_columns( *[ f"Column {n}" for n in range(100)])
        table.add_row(*[ str(n) for n in range(100)])
        return table

    def compose(self) -> ComposeResult:
        with Horizontal():
            with Vertical():
                yield self.populate(DataTable())
            with Vertical():
                yield self.populate(DataTable(classes="fix-height"))

if __name__ == "__main__":
    SingleRowTableApp().run()
