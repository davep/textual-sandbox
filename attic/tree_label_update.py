"""https://github.com/Textualize/textual/issues/2698"""

from textual.app     import App, ComposeResult
from textual.widgets import Header, Footer, Tree

class TreeNodeUpdateApp( App[ None ] ):

    BINDINGS = [
        ( "a", "add", "" ),
    ]

    def compose( self ) -> ComposeResult:
        yield Header()
        yield Tree( "100" )
        yield Footer()

    def on_mount( self ) -> None:
        for n in range( 10 ):
            node = self.query_one( Tree ).root.add( str( n ), expand=True )
            for m in range( 10 ):
                node.add_leaf( str( m ) )

    def action_add( self ):
        node = self.query_one( Tree ).cursor_node
        node.label = str( int( str( node.label ) ) + 1 )
#        self.query_one( Tree ).refresh()

if __name__ == "__main__":
    TreeNodeUpdateApp().run()
