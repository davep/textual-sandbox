from pathlib import Path

from textual.app          import App, ComposeResult
from textual.widgets      import DirectoryTree
from textual.widgets.tree import TreeNode

class RefreshableDirectoryTree( DirectoryTree ):

    def reload_directory( self, node: TreeNode ) -> None:
        node.remove_children()
        node.data.loaded = False
        self._add_to_load_queue(node)

class RefreshingDirTree( App[ None ] ):

    BINDINGS = [
        ( "r", "reload" )
    ]

    def compose( self ) -> ComposeResult:
        yield RefreshableDirectoryTree( Path.home() )

    def action_reload( self ) -> None:
        tree = self.query_one( RefreshableDirectoryTree )
        if tree.cursor_node is not None:
            tree.reload_directory( tree.cursor_node )

if __name__ == "__main__":
    RefreshingDirTree().run()
