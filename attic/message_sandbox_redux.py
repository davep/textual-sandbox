"""Testing from-code message posting.

https://github.com/Textualize/textual/issues/3869
"""

from pathlib import Path

from textual import on
from textual.app import App, ComposeResult
from textual.containers import Horizontal
from textual.coordinate import Coordinate
from textual.message import Message
from textual.widgets import (
    Button,
    Checkbox,
    Collapsible,
    DataTable,
    DirectoryTree,
    Input,
    Label,
    ListItem,
    ListView,
    Log,
    Markdown,
    OptionList,
    RadioButton,
    RadioSet,
    Rule,
    Select,
    SelectionList,
    Switch,
    TabbedContent,
    TabPane,
    TextArea,
    Tree,
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


class ListViewSandbox(TabPane):
    DEFAULT_CSS = """
    ListViewSandbox {
        ListView {
            height: 1fr;
        }
    }
    """

    def __init__(self, *args, **kwargs) -> None:
        super().__init__("ListView", *args, **kwargs)

    def compose(self) -> ComposeResult:
        yield Button("Go to 3", id="option-jump")
        yield ListView(*[ListItem(Label(f"This is option {n}")) for n in range(20)])

    @on(Button.Pressed, "#option-jump")
    def more_input(self) -> None:
        self.query_one(ListView).index = 3


class OptionListSandbox(TabPane):
    DEFAULT_CSS = """
    OptionListSandbox {
        OptionList {
            height: 1fr;
        }
    }
    """

    def __init__(self, *args, **kwargs) -> None:
        super().__init__("OptionList", *args, **kwargs)

    def compose(self) -> ComposeResult:
        yield Button("Go to 3", id="option-jump")
        yield OptionList(*[f"This is option {n}" for n in range(20)])

    @on(Button.Pressed, "#option-jump")
    def more_input(self) -> None:
        self.query_one(OptionList).highlighted = 3


class SelectSandbox(TabPane):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__("Select", *args, **kwargs)

    def compose(self) -> ComposeResult:
        yield Button("Go to 3", id="option-jump")
        yield Select[int](((data[1], data[0]) for data in DATA[1:]))

    @on(Button.Pressed, "#option-jump")
    def more_input(self) -> None:
        self.query_one(Select).value = 3


class SelectionListSandbox(TabPane):
    DEFAULT_CSS = """
    SelectionListSandbox {
        SelectionList {
            height: 1fr;
        }
        Horizontal {
            height: auto;
        }
    }
    """

    def __init__(self, *args, **kwargs) -> None:
        super().__init__("SelectionList", *args, **kwargs)

    def compose(self) -> ComposeResult:
        with Horizontal():
            yield Button("Go to 3", id="option-jump")
            yield Button("Toggle 3", id="toggle")
            yield Button("Select 3", id="select")
            yield Button("Deselect 3", id="deselect")
        yield SelectionList[int](*[(f"This is selection {n}", n) for n in range(20)])

    @on(Button.Pressed, "#option-jump")
    def more_input(self) -> None:
        self.query_one(SelectionList).highlighted = 3

    @on(Button.Pressed, "#toggle")
    def toggle_a_thing(self) -> None:
        self.query_one(SelectionList).toggle(3)

    @on(Button.Pressed, "#select")
    def select_a_thing(self) -> None:
        self.query_one(SelectionList).select(3)

    @on(Button.Pressed, "#deselect")
    def deselect_a_thing(self) -> None:
        self.query_one(SelectionList).deselect(3)


class SwitchSandbox(TabPane):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__("Switch", *args, **kwargs)

    def compose(self) -> ComposeResult:
        yield Button("Toggle", id="toggle")
        yield Switch()

    @on(Button.Pressed, "#toggle")
    def toggle_the_thing(self) -> None:
        self.query_one(Switch).value = not self.query_one(Switch).value


class ToggleButtonSandbox(TabPane):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__("Toggle Buttons", *args, **kwargs)

    def compose(self) -> ComposeResult:
        yield Button("Toggle checkbox", id="toggle-checkbox")
        yield Checkbox("Test checkbox")
        yield Rule()
        yield Button("Toggle radio button", id="toggle-radiobutton")
        yield RadioButton("Test radio button", id="test-radiobutton")
        yield Rule()
        yield Button("Tick #2", id="change-radioset")
        with RadioSet():
            yield RadioButton("One")
            yield RadioButton("Two", id="tester")
            yield RadioButton("Three")

    @on(Button.Pressed, "#toggle-checkbox")
    def toggle_checkbox(self) -> None:
        self.query_one(Checkbox).value = not self.query_one(Checkbox).value

    @on(Button.Pressed, "#toggle-radiobutton")
    def toggle_radiobutton(self) -> None:
        radio_button = self.query_one("#test-radiobutton", RadioButton)
        radio_button.value = not radio_button.value

    @on(Button.Pressed, "#change-radioset")
    def change_radioset(self) -> None:
        self.query_one("#tester", RadioButton).value = True


class TextAreaSandbox(TabPane):
    DEFAULT_CSS = """
    TextAreaSandbox {
        Horizontal {
            height: auto;
        }
    }
    """

    def __init__(self, *args, **kwargs) -> None:
        super().__init__("TextArea", *args, **kwargs)

    def compose(self) -> ComposeResult:
        with Horizontal():
            yield Button("Set the text", id="paste")
            yield Button("Load text", id="load")
            yield Button("Select all", id="select-all")
        yield TextArea(language="python")

    @on(Button.Pressed, "#paste")
    def set_text(self) -> None:
        self.query_one(TextArea).text = Path(__file__).read_text()

    @on(Button.Pressed, "#load")
    def load_text(self) -> None:
        self.query_one(TextArea).load_text(Path(__file__).read_text())

    @on(Button.Pressed, "#select-all")
    def select_all_text(self) -> None:
        self.query_one(TextArea).select_all()


class TreeSandbox(TabPane):
    DEFAULT_CSS = """
    TreeSandbox {
        Horizontal {
            height: auto;
        }
    }
    """

    def __init__(self, *args, **kwargs) -> None:
        super().__init__("Tree", *args, **kwargs)

    def compose(self) -> ComposeResult:
        with Horizontal():
            yield Button("Expand Root", id="expand")
            yield Button("Collapse Root", id="collapse")
            yield Button("Highlight Root", id="highlight")
        yield Tree("Root")

    def on_mount(self) -> None:
        tree = self.query_one(Tree)
        child = tree.root.add("Node")
        for n in range(5):
            child.add_leaf(f"Leaf {n}")

    @on(Button.Pressed, "#expand")
    def expand_root(self) -> None:
        self.query_one(Tree).root.expand()

    @on(Button.Pressed, "#collapse")
    def collapse_root(self) -> None:
        self.query_one(Tree).root.collapse()

    @on(Button.Pressed, "#highlight")
    def highlight_root(self) -> None:
        self.query_one(Tree).select_node(self.query_one(Tree).root)


class MarkdownSandbox(TabPane):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__("Markdown", *args, **kwargs)

    def compose(self) -> ComposeResult:
        yield Button("Update TOC")
        yield Markdown("# This is some markdown\n\nReally, this is Markdown.")

    @on(Button.Pressed)
    def update_toc(self) -> None:
        self.query_one(Markdown).update("")


class DirectoryTreeSandbox(TabPane):
    DEFAULT_CSS = """
    DirectoryTreeSandbox {
        Horizontal {
            height: auto;
        }
    }
    """

    def __init__(self, *args, **kwargs) -> None:
        super().__init__("DirectoryTree", *args, **kwargs)

    def compose(self) -> ComposeResult:
        with Horizontal():
            yield Button("Expand Root", id="expand")
            yield Button("Collapse Root", id="collapse")
            yield Button("Highlight Root", id="highlight")
        yield DirectoryTree("/Users/davep")

    @on(Button.Pressed, "#expand")
    def expand_root(self) -> None:
        self.query_one(DirectoryTree).root.expand()

    @on(Button.Pressed, "#collapse")
    def collapse_root(self) -> None:
        self.query_one(DirectoryTree).root.collapse()

    @on(Button.Pressed, "#highlight")
    def highlight_root(self) -> None:
        self.query_one(DirectoryTree).select_node(self.query_one(DirectoryTree).root)


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
            yield ListViewSandbox()
            yield OptionListSandbox()
            yield SelectSandbox()
            yield SelectionListSandbox()
            yield SwitchSandbox()
            yield ToggleButtonSandbox()
            yield TextAreaSandbox()
            yield TreeSandbox()
            yield MarkdownSandbox()
            yield DirectoryTreeSandbox()
        yield Log()

    @on(Checkbox.Changed)
    @on(Collapsible.Toggled)
    @on(DataTable.CellHighlighted)
    @on(DataTable.CellSelected)
    @on(DataTable.ColumnHighlighted)
    @on(DataTable.ColumnSelected)
    @on(DataTable.HeaderSelected)
    @on(DataTable.RowHighlighted)
    @on(DataTable.RowLabelSelected)
    @on(DataTable.RowSelected)
    @on(Input.Changed)
    @on(ListView.Highlighted)
    @on(OptionList.OptionHighlighted)
    @on(RadioButton.Changed)
    @on(RadioSet.Changed)
    @on(Select.Changed)
    @on(SelectionList.SelectedChanged)
    @on(SelectionList.SelectionHighlighted)
    @on(SelectionList.SelectionToggled)
    @on(Switch.Changed)
    @on(TextArea.Changed)
    @on(TextArea.SelectionChanged)
    @on(Tree.NodeHighlighted)
    @on(Tree.NodeSelected)
    @on(Tree.NodeExpanded)
    @on(Tree.NodeCollapsed)
    @on(Markdown.TableOfContentsUpdated)
    @on(Markdown.TableOfContentsSelected)
    @on(DirectoryTree.FileSelected)
    @on(DirectoryTree.DirectorySelected)
    def log_message(self, message: Message) -> None:
        self.query_one(Log).write_line(f"{message}")


if __name__ == "__main__":
    MessageSandboxApp().run()

### message_sandbox_redux.py ends here
