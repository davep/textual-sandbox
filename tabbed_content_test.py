from textual            import on
from textual.app        import App, ComposeResult
from textual.reactive   import reactive
from textual.containers import Horizontal
from textual.widgets    import TabbedContent, TabPane, Button, TextLog, ContentSwitcher

class TabbedContentTester( App[ None ] ):

    CSS = """
    Screen > Horizontal > * {
        width: 1fr;
    }
    """

    tab_id: reactive[ int ] = reactive( 0 )

    BINDINGS = [
        ( "space", "add_pane" ),
        ( "i", "insert_pane" ),
        ( "delete", "del_pane" ),
        ( "c", "clear" )
    ]

    def compose( self ) -> ComposeResult:
        with Horizontal():
            with TabbedContent():
                for _ in range( 5 ):
                    with TabPane( f"Tab {self.tab_id}" ):
                        yield Button( f"Button {self.tab_id}" )
                    self.tab_id += 1
            yield TextLog()

    async def action_add_pane( self ) -> None:
        await self.query_one( TabbedContent ).add_pane(
            TabPane(
                f"Tab {self.tab_id}",
                Button( f"New Button {self.tab_id}" )
            )
        )
        self.tab_id += 1

    async def action_insert_pane( self ) -> None:
        await self.query_one( TabbedContent ).add_pane(
            TabPane(
                f"Inserted Tab {self.tab_id}",
                Button( f"New Inserted Button {self.tab_id}" )
            ),
            before=self.query_one( ContentSwitcher ).children[0]
        )
        self.tab_id += 1


    async def action_del_pane( self ) -> None:
        if self.query_one( TabbedContent ).tab_count:
            await self.query_one( TabbedContent ).remove_pane(
                self.query_one( TabbedContent ).active
            )

    async def action_clear( self ) -> None:
        await self.query_one( TabbedContent ).clear_panes()

    @on(TabbedContent.TabActivated)
    @on(TabbedContent.Cleared)
    def event_log( self, event: object ) -> None:
        self.query_one( TextLog ).write( f"{event!r}" )

if __name__ == "__main__":
    TabbedContentTester().run()
