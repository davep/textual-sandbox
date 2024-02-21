from textual.app import App, ComposeResult
from textual.widgets import Tree


class TreeCursorNodeApp(App[None]):

    BINDINGS = [
        ("c", "show"),
    ]

    def compose(self) -> ComposeResult:
        yield Tree("Root")

    def on_mount(self) -> None:
        tree = self.query_one(Tree)
        for n in range(10):
            node = tree.root.add(f"Node {n}")
            for m in range(10):
                node.add_leaf(f"Node {n}-{m}")

    def action_show(self) -> None:
        self.notify(f"{self.query_one(Tree).cursor_node}")


if __name__ == "__main__":
    TreeCursorNodeApp().run()

### cursor_node_example.py ends here
