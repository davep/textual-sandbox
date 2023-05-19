from pathlib import Path

from textual.app        import App, ComposeResult
from textual.binding    import Binding
from textual.containers import Grid, Vertical
from textual.widgets    import Footer, DirectoryTree, Label

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
        yield DirectoryTree( Path("~/develop").expanduser(), id=self.id )

    def on_mount( self ) -> None:
        self.query_one( DirectoryTree ).border_title = self.id

    def action_reload(self) -> None:
        self.query_one( DirectoryTree ).reload()

    def action_expand_all(self) -> None:
        self.query_one( DirectoryTree ).root.expand_all()

class DirTreeExplorer( App[ None ] ):

    CSS = """
    Grid {
        grid-size: 3;
    }
    """

    BINDINGS = [
        Binding( "ctrl+a", "expand_all" ),
    ]

    def compose( self ) -> ComposeResult:
        with Grid():
            for n in range( 9 ):
                yield Browser(id=f"directory-tree-{n}")
        yield Footer()

    def on_mount( self ) -> None:
        self.query( DirectoryTree ).first().focus()

    def action_expand_all(self):
        for tree in self.query( DirectoryTree ):
            tree.root.expand_all()

if __name__ == "__main__":
    DirTreeExplorer().run()
