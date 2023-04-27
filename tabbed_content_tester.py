from textual.app        import App, ComposeResult
from textual.binding    import Binding
from textual.containers import Horizontal, Vertical
from textual.widgets    import Header, Footer, TabbedContent, TabPane, Tabs, Label

class StandardTabs( Vertical ):

    def compose( self ) -> ComposeResult:
        with TabbedContent():
            for n in range( 10 ):
                with TabPane( f"Tab {n}" ):
                    yield Label( f"This is tab {n}" )

class SelfSwitchTabs( StandardTabs ):

    BINDINGS = [
        Binding( "a", "previous", "Previous" ),
        Binding( "d", "next", "Next" ),
    ]

    def action_previous(self) -> None:
        self.query_one(Tabs).action_previous_tab()

    def action_next(self) -> None:
        self.query_one(Tabs).action_next_tab()

class TabbedContentTesterApp( App[ None ] ):

    CSS = """
    StandardTabs:focus-within {
        background: $panel;
    }
    """

    def compose( self ) -> ComposeResult:
        yield Header()
        with Horizontal():
            yield StandardTabs()
            yield SelfSwitchTabs()
        yield Footer()

if __name__ == "__main__":
    TabbedContentTesterApp().run()
