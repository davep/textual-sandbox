"""Example of adding extra stuff to a DirectoryTree entry."""

from pathlib import Path

from rich.style import Style
from rich.text import Text
from textual.app import App, ComposeResult
from textual.types import DirEntry
from textual.widgets import DirectoryTree
from textual.widgets.tree import TreeNode


class DirectoryTreeEx(DirectoryTree):
    def file_icon(self, path: Path) -> str:
        return {
            ".py": "🐍",
            ".rst": "🦀",
            # etc...
        }.get(path.suffix.lower(), "📄")

    def render_label(
        self, node: TreeNode[DirEntry], base_style: Style, style: Style
    ) -> Text:
        # Get the label from DirectoryTree
        label = super().render_label(node, base_style, style)
        # If this isn't a directory...
        if node.data is not None and not node._allow_expand:
            # ...strip off the plain old paper sheet icon and add one
            # depending on the extension...
            label = Text.assemble(self.file_icon(node.data.path), label.divide([1])[1])
        return label


class DirTreeLabelsApp(App[None]):
    def compose(self) -> ComposeResult:
        yield DirectoryTreeEx(".")


if __name__ == "__main__":
    DirTreeLabelsApp().run()

### dir_tree_labels.py ends here
