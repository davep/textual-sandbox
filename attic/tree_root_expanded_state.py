"""Tester for https://github.com/Textualize/textual/issues/3557"""

from textual.app import App, ComposeResult
from textual.widgets import Tree


class TreeRootExpandedStateApp(App[None]):
    CSS = """
    Screen {
        layout: horizontal;
    }
    """

    BINDINGS = [
        ("c", "clear"),
        ("r", "repopulate"),
    ]

    @staticmethod
    def _populate(tree: Tree) -> Tree:
        for n in range(10):
            child = tree.root.add(f"Top level {n}")
            for m in range(10):
                child.add_leaf(f"Leaf {n}-{m}")
        return tree

    def compose(self) -> ComposeResult:
        for name in ("one", "two", "three", "four"):
            yield self._populate(Tree(name.capitalize(), id=name))

    def action_clear(self) -> None:
        if isinstance(self.screen.focused, Tree):
            self.screen.focused.clear()

    def action_repopulate(self) -> None:
        if isinstance(self.screen.focused, Tree):
            self._populate(self.screen.focused.clear())


if __name__ == "__main__":
    TreeRootExpandedStateApp().run()

### tree_root_expanded_state.py ends here
