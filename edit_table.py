"""Example of editing a cell in a DataTable."""

from functools import partial

from textual import on
from textual.app import App, ComposeResult
from textual.screen import ModalScreen
from textual.widgets import DataTable, Input

ROWS = [
    ("lane", "swimmer", "country", "time"),
    (4, "Joseph Schooling", "Singapore", 50.39),
    (2, "Michael Phelps", "United States", 51.14),
    (5, "Chad le Clos", "South Africa", 51.14),
    (6, "László Cseh", "Hungary", 51.14),
    (3, "Li Zhuhao", "China", 51.26),
    (8, "Mehdy Metella", "France", 51.58),
    (7, "Tom Shields", "United States", 51.73),
    (1, "Aleksandr Sadovnikov", "Russia", 51.84),
    (10, "Darren Burns", "Scotland", 51.84),
]


class CellEdit(ModalScreen[str]):

    CSS = """
    CellEdit {
        align: center middle;
    }

    CellEdit Input {
        width: 60%;
    }
    """

    def __init__(self, edit_event: DataTable.CellSelected) -> None:
        super().__init__()
        self._edit_event = edit_event

    def compose(self) -> ComposeResult:
        yield Input(str(self._edit_event.value))

    @on(Input.Submitted)
    def finished_edit(self, event: Input.Submitted):
        self.dismiss(event.value)


class TableApp(App):
    def compose(self) -> ComposeResult:
        yield DataTable()

    def on_mount(self) -> None:
        table = self.query_one(DataTable)
        table.add_columns(*ROWS[0])
        table.add_rows(ROWS[1:])

    def update_cell(self, event: DataTable.CellSelected, new_value: str) -> None:
        self.query_one(DataTable).update_cell(event.cell_key.row_key, event.cell_key.column_key, new_value)

    @on(DataTable.CellSelected)
    def edit_cell(self, event: DataTable.CellSelected) -> None:
        self.push_screen(CellEdit(event), callback=partial(self.update_cell, event))

if __name__ == "__main__":
    TableApp().run()

### edit_table.py ends here
