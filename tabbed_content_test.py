from textual            import on
from textual.app        import App, ComposeResult
from textual.reactive   import reactive
from textual.containers import Horizontal
from textual.widgets    import TabbedContent, TabPane, Button, TextLog

class TabbedContentTester( App[ None ] ):

    CSS = """
    Screen > Horizontal > * {
        width: 1fr;
    }
    """

    tab_id: reactive[ int ] = reactive( 0 )

    BINDINGS = [
        ( "space", "add_pane" ),
        ( "delete", "del_pane" ),
        ( "c", "clear" )
    ]

    def compose( self ) -> ComposeResult:
        with Horizontal():
            with TabbedContent():
                for _ in range( 5 ):
                    with TabPane( self.next_id ):
                        yield Button( f"Button {self.tab_id}" )
            yield TextLog()

    @property
    def next_id( self ) -> str:
        try:
            return f"Tab {self.tab_id}"
        finally:
            self.tab_id += 1

    def action_add_pane( self ) -> None:
        self.query_one( TabbedContent ).add_pane(
            TabPane(
                self.next_id,
                Button( f"New Button {self.tab_id}" ),
                id=f"added-later-{self.tab_id}"
            )
        )

    def action_del_pane( self ) -> None:
        if self.query_one( TabbedContent ).tab_count:
            self.query_one( TabbedContent ).remove_pane(
                self.query_one( TabbedContent ).active
            )

    def action_clear( self ) -> None:
        self.query_one( TabbedContent ).clear_panes()

    @on(TabbedContent.TabActivated)
    @on(TabbedContent.Cleared)
    def event_log( self, event: object ) -> None:
        self.query_one( TextLog ).write( f"{event!r}" )

if __name__ == "__main__":
    TabbedContentTester().run()
