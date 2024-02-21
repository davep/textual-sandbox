from textual.app import App, ComposeResult
from textual.containers import Horizontal, Vertical, Grid
from textual.widgets import (
    Header,
    Footer,
    Input,
    Button,
    Tree,
    DataTable,
    Static,
    ListView,
    ListItem,
    Label,
    DirectoryTree,
    TextLog,
    Switch,
)
from textual.events import MouseMove
from textual.css.query import NoMatches


class MouseWatcher(Static):

    DEFAULT_CSS = """
    MouseWatcher {
        height: 100%;
        width: 100%;
        background: green;
    }
    """

    def on_mouse_move(self, event: MouseMove) -> None:
        self.update(repr(event))


class DisableTestingApp(App[None]):

    CSS = """
    Horizontal {
        height: auto;
        border-bottom: solid red;
    }

    Horizontal > Button {
        width: 1fr;
        margin-left: 1;
        margin-right: 1;
    }

    Grid {
        grid-size: 2 7;
    }

    Grid > Button {
        width: 100%;
        height: 100%;
    }

    #inputs {
        height: auto;
    }

    ListView {
        height: 100%;
    }
    """

    @property
    def tree(self) -> Tree:
        tree = Tree(label="This is a test tree")
        for n in range(10):
            node = tree.root.add(f"Branch {n}")
            for m in range(10):
                node.add_leaf(f"Leaf {m} of branch {n}")
        return tree

    @property
    def data_table(self) -> DataTable:
        data_table = DataTable()
        data_table.add_columns("Column 1", "Column 2", "Column 3", "Column 4")
        data_table.add_rows(
            [(str(n), str(n * 10), str(n * 100), str(n * 1000)) for n in range(100)]
        )
        return data_table

    @property
    def list_view(self) -> ListView:
        return ListView(*[ListItem(Label(f"This is list item {n}")) for n in range(20)])

    def compose(self) -> ComposeResult:
        yield Header()
        yield Vertical(
            Horizontal(Button("Disable", id="disable"), Button("Enable", id="enable")),
            Grid(
                Button("Default Button"),
                Button("Primary Button", variant="primary"),
                Button("Success Button", variant="success"),
                Button("Warning Button", variant="warning"),
                Button("Error Button", variant="error"),
                Vertical(
                    Input("", placeholder="Empty Input"),
                    Input("Filled Input", placeholder="Filled Input"),
                    id="inputs",
                ),
                self.tree,
                self.data_table,
                Switch(),
                MouseWatcher(),
                self.list_view,
                DirectoryTree("."),
                TextLog(),
            ),
        )
        yield Footer()

    async def on_event(self, event) -> None:
        await super().on_event(event)
        try:
            self.query_one(TextLog).write(event)
        except NoMatches:
            pass

    def on_button_pressed(self, event: Button.Pressed) -> None:
        if event.button.id in ("enable", "disable"):
            self.query_one(Grid).disabled = event.button.id == "disable"


if __name__ == "__main__":
    DisableTestingApp().run()

### disable_tester.py ends here
