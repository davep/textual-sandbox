from textual.app        import App, ComposeResult
from textual.binding    import Binding
from textual.containers import Horizontal, VerticalScroll
from textual.widgets    import Header, Footer, TabbedContent, TabPane, Tabs, Input

class StandardTabs( VerticalScroll ):

    def compose( self ) -> ComposeResult:
        with TabbedContent():
            for n in range( 10 ):
                with TabPane( f"Tab {n}" ):
                    for m in range(30):
                        yield Input( placeholder=f"{n:2}:{m:2} - Here's an input to make this more busy" )

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
