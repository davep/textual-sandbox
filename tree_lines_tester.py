"""https://github.com/Textualize/textual/issues/2397"""

from textual.app          import App, ComposeResult
from textual.containers   import Horizontal
from textual.widgets      import Header, Footer, Tree
from textual.widgets.tree import TreeNode

class TreeLinesTestApp( App[ None ] ):

    CSS = """
    Tree {
        padding: 1 2;
        border: thick red 20%;
    }

    Tree:focus {
        border: thick yellow 50%;
    }
    """

    def compose( self ) -> ComposeResult:
        yield Header()
        with Horizontal():
            yield Tree("Root", id="root")
            yield Tree("Root", id="no-root")
        yield Footer()

    def populate( self, node: TreeNode, limit: int=4 ) -> Tree:
        for n in range( limit ):
            if limit > 1:
                self.populate( node.add( str( n ) ), limit-1 )
            else:
                node.add_leaf( str( n ) )
        return node.tree

    def on_mount( self ) -> None:
        self.query_one( "#no-root", Tree ).show_root = False
        self.populate( self.query_one( "#root", Tree ).root ).root.expand_all()
        self.populate( self.query_one( "#no-root", Tree ).root ).root.expand_all()
        self.query_one( "#root", Tree ).focus()

if __name__ == "__main__":
    TreeLinesTestApp().run()
