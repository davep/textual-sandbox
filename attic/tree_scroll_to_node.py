from textual.app import App, ComposeResult
from textual.widgets import Tree


class ScrollToNode(App[None]):

    def compose(self) -> ComposeResult:
        yield Tree("Root")

    def on_mount(self) -> None:
        tree = self.query_one(Tree)
        for n in range(100):
            outer = tree.root.add(str(n))
            for m in range(10):
                added = outer.add_leaf(str(m))
        tree.root.expand_all()
        self.call_after_refresh(tree.scroll_to_node, added)


if __name__ == "__main__":
    ScrollToNode().run()

### tree_scroll_to_node.py ends here
