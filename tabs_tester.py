from textual            import on
from textual.app        import App, ComposeResult
from textual.binding    import Binding
from textual.containers import Center
from textual.widgets    import Tab, Tabs, Label, TextLog

class TabsTesterApp( App[ None ] ):

    BINDINGS = [
        Binding( "space", "add" ),
        Binding( "i", "insert" ),
        Binding( "a", "after" ),
        Binding( "delete", "delete" ),
        Binding( "c", "clear" ),
    ]

    def compose( self ) -> ComposeResult:
        yield Tabs(
            *[ Tab( f"This is tab {n}" ) for n in range( 5 ) ]
        )
        with Center():
            yield Label()
        yield TextLog()

    @on( Tabs.TabActivated )
    def show_current_tab( self, event: Tabs.TabActivated ) -> None:
        self.query_one( Label ).update( f"{event.tab!r}" )

    async def action_add( self ) -> None:
        await self.query_one( Tabs ).add_tab( "New Tab" )

    async def action_insert( self ) -> None:
        await self.query_one( Tabs ).add_tab( "Inserted Before Tab", before=self.query_one( Tabs ).active_tab )

    async def action_after( self ) -> None:
        await self.query_one( Tabs ).add_tab( "Inserted After Tab", after=self.query_one( Tabs ).active_tab )

    async def action_delete( self ) -> None:
        await self.query_one( Tabs ).remove_tab( self.query_one( Tabs ).active_tab )

    async def action_clear( self ) -> None:
        await self.query_one( Tabs ).clear()

    @on( Tabs.TabActivated )
    @on( Tabs.Cleared )
    def log_event( self, event ) -> None:
        self.query_one( TextLog ).write( f"{event!r}" )

if __name__ == "__main__":
    TabsTesterApp().run()
