"""https://github.com/Textualize/textual/issues/2397"""

from textual.app import App, ComposeResult
from textual.containers import Horizontal
from textual.widgets import Header, Footer, Tree
from textual.widgets.tree import TreeNode


class TreeLinesTestApp(App[None]):

    CSS = """
    Tree {
        padding: 1 2;
        border: thick red 20%;
    }

    Tree:focus {
        border: thick yellow 50%;
    }
    """

    BINDINGS = [
        ("delete", "delete_children", "Delete children"),
        ("backspace", "delete_node", "Delete node"),
    ]

    def compose(self) -> ComposeResult:
        yield Header()
        with Horizontal():
            yield Tree("Root", id="root")
            yield Tree("Root", id="no-root")
        yield Footer()

    def populate(self, node: TreeNode, limit: int = 4) -> Tree:
        for n in range(limit):
            if limit > 1:
                self.populate(node.add(str(n)), limit - 1)
            else:
                node.add_leaf(str(n))
        return node.tree

    def on_mount(self) -> None:
        root = self.query_one("#root", Tree)
        no_root = self.query_one("#no-root", Tree)
        no_root.show_root = False
        self.populate(root.root).root.expand_all()
        self.populate(no_root.root).root.expand_all()
        root.focus()
        self.populate(self.query_one("#no-root", Tree).root).root.expand_all()
        root.border_title = f"{len(root._tree_nodes)}"
        no_root.border_title = f"{len(no_root._tree_nodes)}"

    def action_delete_children(self) -> None:
        if isinstance(self.focused, Tree) and self.focused.cursor_node is not None:
            self.focused.cursor_node.remove_children()
            self.focused.border_title = f"{len(self.focused._tree_nodes)}"

    def action_delete_node(self) -> None:
        if isinstance(self.focused, Tree) and self.focused.cursor_node is not None:
            self.focused.cursor_node.remove()
            self.focused.border_title = f"{len(self.focused._tree_nodes)}"

    def on_tree_node_highlighted(self, event: Tree.NodeHighlighted) -> None:
        event.node.tree.border_title = f"cursor_line = {event.node.tree.cursor_line}"


if __name__ == "__main__":
    TreeLinesTestApp().run()
