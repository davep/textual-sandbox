from textual.app import App, ComposeResult
from textual.widgets import DataTable

class DataTableColumnSizesApp(App[None]):

    CSS = """
    DataTable {
        height: 1fr;
    }
    """

    BINDINGS = [
        ("space", "show_column_sizes"),
    ]

    def compose(self) -> ComposeResult:
        yield DataTable()

    def on_mount(self) -> None:
        table = self.query_one(DataTable)
        table.add_column("Not Fixed")
        table.add_column("Also not fixed but with a long title")
        table.add_column("This one is fixed", width=50)
        for n in range(1_000):
            table.add_row(str(n), f"Second {n}",f"Final {n}")

    def action_show_column_sizes(self) -> None:
        self.notify(f"The table's width is: {self.query_one(DataTable).size.width}")
        for column in self.query_one(DataTable).columns.values():
            self.notify(
                f"Width: {column.width}\nRender width: {column.render_width}",
                title=f"Column: {column.label}",
                timeout=10
            )

if __name__ == "__main__":
    DataTableColumnSizesApp().run()
