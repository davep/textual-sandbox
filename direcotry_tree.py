"""Example of a DirTree that shows abs root."""

from pathlib import Path

from textual.app import App, ComposeResult
from textual.types import DirEntry
from textual.widgets import DirectoryTree


class AbsDirectoryTree(DirectoryTree):

    def on_mount(self) -> None:
        assert isinstance(self.root.data, DirEntry)
        self.root.label = str(self.root.data.path.absolute())


class DirectoryTreeApp(App[None]):

    def compose(self) -> ComposeResult:
        yield AbsDirectoryTree(Path("."))


if __name__ == "__main__":
    DirectoryTreeApp().run()

### direcotry_tree.py ends here
