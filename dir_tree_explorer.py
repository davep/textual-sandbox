from textual.app        import App, ComposeResult
from textual.binding    import Binding
from textual.containers import Horizontal, Vertical
from textual.widgets    import Footer, DirectoryTree, Input, Label

class Browser( Vertical ):

    BINDINGS = [
        Binding( "r", "reload", "Reload" ),
        Binding( "a", "expand_all", "Expand All"),
    ]

    DEFAULT_CSS = """
    Browser DirectoryTree {
        border: tall $background;
    }

    Browser DirectoryTree:focus {
        border: tall $accent;
    }

    Label {
        margin-left: 1;
    }
    """

    def compose( self ) -> ComposeResult:
        yield Input( placeholder="Enter a new root here" )
        yield DirectoryTree( "." )
        yield Label( "Hello!" )

    def on_input_submitted( self, event: Input.Submitted ) -> None:
        self.query_one( DirectoryTree ).path = event.value
        self.query_one( DirectoryTree ).focus()

    def on_directory_tree_file_selected( self, event: DirectoryTree.FileSelected ) -> None:
        self.query_one( Label ).update( f"{event.path!r}" )

    def action_reload(self) -> None:
        self.query_one( DirectoryTree ).reload()

    def action_expand_all(self) -> None:
        self.query_one( DirectoryTree ).root.expand_all()

class DirTreeExplorer( App[ None ] ):

    def compose( self ) -> ComposeResult:
        with Horizontal():
            yield Browser()
            yield Browser()
            yield Browser()
        yield Footer()

    def on_mount( self ) -> None:
        self.query( Input ).first().focus()

if __name__ == "__main__":
    DirTreeExplorer().run()
