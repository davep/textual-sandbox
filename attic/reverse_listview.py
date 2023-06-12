from textual.app      import App, ComposeResult
from textual.widgets  import Header, Footer, ListView, ListItem, Label
from textual.widget   import AwaitMount
from textual.reactive import var

class ReverseListView( ListView ):

    def prepend( self, item: ListItem ) -> AwaitMount:
        await_mount = self.mount( item, before=0 )
        if len( self ) == 1:
            self.index = 0
        return await_mount

class ReverseListViewApp( App[ None ] ):

    counter = var(0)

    BINDINGS = [
        ( "space", "new", "Add a new ListItem" ),
    ]

    def compose( self ) -> ComposeResult:
        yield Header()
        yield ReverseListView()
        yield Footer()

    def action_new( self ) -> None:
        self.query_one( ReverseListView ).prepend( ListItem( Label( f"Item {self.counter}" ) ) )
        self.counter += 1

if __name__ == "__main__":
    ReverseListViewApp().run()
