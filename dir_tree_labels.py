"""Example of adding extra stuff to a DirectoryTree entry."""

from rich.style import Style
from rich.text import Text
from textual.app import App, ComposeResult
from textual.types import DirEntry
from textual.widgets import DirectoryTree
from textual.widgets.tree import TreeNode


class MyDirectoryTree(DirectoryTree):
    def render_label(
        self, node: TreeNode[DirEntry], base_style: Style, style: Style
    ) -> Text:
        return Text.assemble(
            super().render_label(node, base_style, style), " LOOK I ADDED THIS MYSELF!"
        )


class DirTreeLabelsApp(App[None]):
    def compose(self) -> ComposeResult:
        yield MyDirectoryTree(".")


if __name__ == "__main__":
    DirTreeLabelsApp().run()

### dir_tree_labels.py ends here
