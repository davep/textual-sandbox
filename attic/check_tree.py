"""https://github.com/Textualize/textual/discussions/2609"""

from textual.app import App, ComposeResult
from textual.widgets import Header, Footer, Tree


class ToggleTree(Tree[bool]):

    def on_tree_node_selected(self, event: Tree.NodeSelected) -> None:
        if not event.node.children:
            event.node.data = not event.node.data
            if event.node.data:
                event.node.label = ":thumbsup:"
            else:
                event.node.label = ":thumbsdown:"
            event.node.tree.refresh()


class CheckTreeApp(App[None]):

    def compose(self) -> ComposeResult:
        yield Header()
        yield ToggleTree("Root")
        yield Footer()

    def on_mount(self) -> None:
        tree = self.query_one(ToggleTree)
        tree.root.add_leaf(":thumbsdown:")
        tree.root.add_leaf(":thumbsdown:")
        tree.root.add_leaf(":thumbsdown:")


if __name__ == "__main__":
    CheckTreeApp().run()
