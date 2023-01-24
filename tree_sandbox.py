from textual.app     import App, ComposeResult
from textual.widgets import Header, Footer, Tree, TreeNode
from textual.binding import Binding

class Sandbox( Tree[ None ] ):
    pass

class TreeSandbox( App[ None ] ):

    CSS = """
    Tree {
        width: 1fr;
    }
    """

    BINDINGS = [
        *[ Binding( str( n ), f"select( {n} )", f"Select {n}" ) for n in range( 10 ) ],
        *[ Binding( f"f{n}", f"expand( {n} )", f"Expand {n}" ) for n in range( 10 ) ],
        Binding( "e", "expand_all", "Expand All" ),
        Binding( "c", "collapse_all", "Collapse All" ),
        Binding( "t", "toggle_all", "Toggle All" ),
    ]


    def __init__( self ):
        super().__init__()
        self.nodes: list[ TreeNode[ None ] ] = []

    def compose( self ) -> ComposeResult:
        yield Header()
        self.sandbox = Sandbox( "Tree Sandbox" )
        yield self.sandbox
        yield Footer()

    def on_mount( self ) -> None:
        for node in range( 10 ):
            self.nodes.append(
                self.sandbox.root.add( f"This is parent node {node}" )
            )
            for child in range( 10 ):
                self.nodes[ -1 ].add_leaf(
                    f"Child node {child}"
                )
        deeply = 0
        node   = self.nodes[ 0 ]
        while deeply < 50:
            node = node.add( "We must go deeper" )
            deeply += 1
        self.sandbox.focus()

    def action_select( self, node: int ) -> None:
        self.sandbox.select_node( self.nodes[ node ] )

    def action_expand( self, node: int ) -> None:
        if self.nodes[ node ].is_expanded:
            self.nodes[ node ].collapse()
        else:
            self.nodes[ node ].expand()

    def action_expand_all( self ) -> None:
        """Expand all"""
        if self.sandbox.cursor_node:
            self.sandbox.cursor_node.expand( expand_all=True )

    def action_collapse_all( self ) -> None:
        """Collapse all"""
        if self.sandbox.cursor_node:
            self.sandbox.cursor_node.collapse( collapse_all=True )

    def action_toggle_all( self ) -> None:
        """Toggle all"""
        if self.sandbox.cursor_node:
            self.sandbox.cursor_node.toggle( toggle_all=True )


if __name__ == "__main__":
    TreeSandbox().run()
