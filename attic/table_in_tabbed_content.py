from textual.app import App, ComposeResult
from textual.widgets import TabbedContent, TabPane, DataTable


class DataTableInTabsApp(App[None]):

    CSS = """
    DataTable {
        height: 1fr;
    }
    """

    def compose(self) -> ComposeResult:
        with TabbedContent():
            with TabPane("Ships", id="ships"):
                yield DataTable()
            with TabPane("Numbers", id="numbers"):
                yield DataTable()

    def on_mount(self) -> None:
        ships = self.query_one("#ships DataTable", DataTable)
        ships.add_columns("Ship", "Captain")
        ships.add_rows(
            (
                ("Serenity", "Malcolm Reynolds"),
                ("USS Enterprise", "Jonathan Archer"),
                ("USS Voyager", "Kathryn Janeway"),
                ("Millennium Falcon", "Landonis Balthazar Calrissian"),
            )
        )
        numbers = self.query_one("#numbers DataTable", DataTable)
        numbers.add_columns("Row", *[f"Column {n+1}" for n in range(10)])
        for row in range(1_000):
            numbers.add_row(*[str(row), *[str(n) for n in range(10)]])


if __name__ == "__main__":
    DataTableInTabsApp().run()

### table_in_tabbed_content.py ends here
