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
        *[ Binding( f"f{n}", f"expand( {n} )", f"Expand {n}" ) for n in range( 10 ) ]
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
        self.sandbox.focus()

    def action_select( self, node: int ) -> None:
        self.sandbox.select_node( self.nodes[ node ] )

    def action_expand( self, node: int ) -> None:
        if self.nodes[ node ].is_expanded:
            self.nodes[ node ].collapse()
        else:
            self.nodes[ node ].expand()

if __name__ == "__main__":
    TreeSandbox().run()
