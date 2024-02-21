"""https://github.com/Textualize/textual/discussions/2961"""

from textual.app import App, ComposeResult
from textual.widgets import DataTable, TabbedContent, TabPane


class DataTableInTabbedContentApp(App[None]):

    CSS = """
    TabbedContent ContentSwitcher, DataTable {
        height: 1fr
    }
    """

    def populate(self, table: DataTable) -> DataTable:
        table.add_columns("Row", *[f"Column {n+1}" for n in range(10)])
        for row in range(1_000):
            table.add_row(*[str(row), *[str(n) for n in range(10)]])
        return table

    def compose(self) -> ComposeResult:
        with TabbedContent():
            with TabPane("Some data"):
                yield self.populate(DataTable())


if __name__ == "__main__":
    DataTableInTabbedContentApp().run()

### dt_in_tabbed_content.py ends here
