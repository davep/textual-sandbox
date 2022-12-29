from textual.app        import App, ComposeResult
from textual.containers import Vertical
from textual.widgets    import Header, Footer, Tree

class WideTree( App[ None ] ):

    CSS = """
    Vertical {
        width: 30;
    }
    Tree {
        width: 1fr;
    }
    """

    def compose( self ) -> ComposeResult:
        yield Header()
        yield Vertical( Tree[ None ]( "Wide Test" ) )
        yield Footer()

    def on_mount( self ) -> None:
        ( node := self.query_one( Tree[ None ] ).root ).expand()
        for n in range( 100 ):
            node = node.add( str( n ), expand=True )
        self.query_one( Tree ).focus()

if __name__ == "__main__":
    WideTree().run()
