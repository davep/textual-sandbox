from textual            import on
from textual.app        import App, ComposeResult
from textual.binding    import Binding
from textual.containers import Center
from textual.widgets    import Tab, Tabs, Label

class TabsTesterApp( App[ None ] ):

    BINDINGS = [
        Binding( "space", "add" ),
        Binding( "delete", "delete" ),
    ]

    def compose( self ) -> ComposeResult:
        yield Tabs(
            *[ Tab( f"This is tab {n}" ) for n in range( 5 ) ]
        )
        with Center():
            yield Label()

    @on( Tabs.TabActivated )
    def show_current_tab( self, event: Tabs.TabActivated ) -> None:
        self.query_one( Label ).update( f"{event.tab!r}" )

    def action_add( self ) -> None:
        self.query_one( Tabs ).add_tab( "New Tab" )

    def action_delete( self ) -> None:
        self.query_one( Tabs ).remove_tab( self.query_one( Tabs ).active_tab )

if __name__ == "__main__":
    TabsTesterApp().run()
