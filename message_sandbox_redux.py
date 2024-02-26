"""Testing from-code message posting.

https://github.com/Textualize/textual/issues/3869
"""

from textual import on
from textual.app import App, ComposeResult
from textual.coordinate import Coordinate
from textual.message import Message
from textual.widgets import (
    Button,
    Collapsible,
    DataTable,
    Input,
    Label,
    Log,
    TabbedContent,
    TabPane,
)

DATA = [
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


class CollapsibleSandbox(TabPane):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__("Collapsible", *args, **kwargs)

    def compose(self) -> ComposeResult:
        yield Button("Toggle from code")
        with Collapsible():
            yield Label("Hello, World!")

    @on(Button.Pressed)
    def toggle_from_code(self) -> None:
        self.query_one(Collapsible).collapsed = not self.query_one(
            Collapsible
        ).collapsed


class DataTableCellSandbox(TabPane):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__("DataTable (Cell)", *args, **kwargs)

    def compose(self) -> ComposeResult:
        yield Button("Select Cell", id="selcell")
        yield DataTable()

    def on_mount(self) -> None:
        table = self.query_one(DataTable)
        table.add_columns(*DATA[0])
        table.add_rows(DATA[1:])

    @on(Button.Pressed, "#selcell")
    def select_cell(self) -> None:
        self.query_one(DataTable).cursor_coordinate = Coordinate(1, 1)


class DataTableRowSandbox(TabPane):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__("DataTable (Row)", *args, **kwargs)

    def compose(self) -> ComposeResult:
        yield Button("Select Row", id="selrow")
        yield DataTable(cursor_type="row")

    def on_mount(self) -> None:
        table = self.query_one(DataTable)
        table.add_columns(*DATA[0])
        table.add_rows(DATA[1:])

    @on(Button.Pressed, "#selrow")
    def select_cell(self) -> None:
        self.query_one(DataTable).cursor_coordinate = Coordinate(1, 1)


class DataTableColumnSandbox(TabPane):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__("DataTable (Column)", *args, **kwargs)

    def compose(self) -> ComposeResult:
        yield Button("Select Column", id="selcol")
        yield DataTable(cursor_type="column")

    def on_mount(self) -> None:
        table = self.query_one(DataTable)
        table.add_columns(*DATA[0])
        table.add_rows(DATA[1:])

    @on(Button.Pressed, "#selcol")
    def select_cell(self) -> None:
        self.query_one(DataTable).cursor_coordinate = Coordinate(1, 1)


class InputSandbox(TabPane):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__("Input", *args, **kwargs)

    def compose(self) -> ComposeResult:
        yield Button("More input", id="input")
        yield Input()

    @on(Button.Pressed, "#input")
    def more_input(self) -> None:
        self.query_one(Input).value += "x"


class MessageSandboxApp(App[None]):
    CSS = """
    TabbedContent {
        height: 1fr;
    }

    Log {
        height: 1fr;
        border-top: solid cornflowerblue;
    }
    """

    def compose(self) -> ComposeResult:
        with TabbedContent():
            yield CollapsibleSandbox()
            yield DataTableCellSandbox()
            yield DataTableRowSandbox()
            yield DataTableColumnSandbox()
            yield InputSandbox()
        yield Log()

    @on(Collapsible.Toggled)
    @on(DataTable.CellHighlighted)
    @on(DataTable.CellSelected)
    @on(DataTable.RowHighlighted)
    @on(DataTable.RowSelected)
    @on(DataTable.ColumnHighlighted)
    @on(DataTable.ColumnSelected)
    @on(DataTable.HeaderSelected)
    @on(DataTable.RowLabelSelected)
    @on(Input.Changed)
    def log_message(self, message: Message) -> None:
        self.query_one(Log).write_line(f"{message}")


if __name__ == "__main__":
    MessageSandboxApp().run()

### message_sandbox_redux.py ends here
