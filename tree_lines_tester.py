"""https://github.com/Textualize/textual/issues/2397"""

from textual.app          import App, ComposeResult
from textual.containers   import Horizontal
from textual.widgets      import Header, Footer, Tree
from textual.widgets.tree import TreeNode

class TreeLinesTestApp( App[ None ] ):

    CSS = """
    Tree {
        border: round red;
    }

    Tree:focus {
        border: double green;
    }
    """

    def compose( self ) -> ComposeResult:
        yield Header()
        with Horizontal():
            yield Tree("Root", id="root")
            yield Tree("Root", id="no-root")
        yield Footer()

    def populate( self, node: TreeNode, limit: int=3 ) -> Tree:
        for n in range( limit ):
            self.populate( node.add( str( n ) ), limit-1 )
        return node.tree

    def on_mount( self ) -> None:
        self.query_one( "#no-root", Tree ).show_root = False
        self.populate( self.query_one( "#root", Tree ).root ).root.expand_all()
        self.populate( self.query_one( "#no-root", Tree ).root ).root.expand_all()

if __name__ == "__main__":
    TreeLinesTestApp().run()
