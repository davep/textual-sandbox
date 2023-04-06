from pathlib import Path

from typing import Iterable

from textual.app        import App, ComposeResult
from textual.containers import Horizontal
from textual.widgets    import Header, Footer, DirectoryTree

class MDDirectoryTree(DirectoryTree):

    def filter_paths(self, paths: Iterable[Path]) -> Iterable[Path]:
        """Filter the paths before adding them to the tree.

        Args:
            paths: The paths to be filtered.

        Returns:
            The filtered paths.
        """
        return [
            path for path in paths
            if not path.name[0] == "." and path.is_dir() or (
                    path.is_file() and path.suffix == ".md"
            )
        ]

class DirTreeFilter( App[ None ] ):

    CSS = """
    DirectoryTree {
        width: 1fr;
    }
    """

    def compose( self ) -> ComposeResult:
        yield Header()
        yield Horizontal(
            DirectoryTree("."),
            MDDirectoryTree(".")
        )
        yield Footer()

if __name__ == "__main__":
    DirTreeFilter().run()
