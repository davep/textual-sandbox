from __future__ import annotations

from textual            import on
from textual.app        import App, ComposeResult
from textual.containers import Horizontal
from textual.widgets    import Header, Footer, Tree, TextLog

class TreeOnApp( App[ None ] ):

    def compose( self ) -> ComposeResult:
        yield Header()
        with Horizontal():
            yield Tree("Root")
            yield TextLog()
        yield Footer()

    def on_mount( self ) -> None:
        for n in range( 10 ):
            node = self.query_one( Tree ).root.add( f"Node {n}" )
            for m in range( 10 ):
                node.add_leaf( f"Sub {n}/{m}" )

    @on( Tree.NodeSelected )
    @on( Tree.NodeHighlighted )
    @on( Tree.NodeExpanded )
    @on( Tree.NodeCollapsed )
    def tree_event( self, event: Tree.NodeSelected | Tree.NodeHighlighted | Tree.NodeExpanded | Tree.NodeCollapsed ) -> None:
        self.query_one( TextLog ).write( f"{event!r}" )

if __name__ == "__main__":
    TreeOnApp().run()
