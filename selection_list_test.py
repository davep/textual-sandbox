from __future__ import annotations

from textual            import on
from textual.app        import App, ComposeResult
from textual.binding    import Binding
from textual.containers import Horizontal, VerticalScroll
from textual.widgets    import Header, Footer, SelectionList, TextLog, OptionList, Pretty

class SelectionListtestApp( App[ None ] ):

    BINDINGS = [
        Binding( "1", "select(1)", "Toggle 1" ),
        Binding( "2", "select(2)", "Toggle 2" ),
        Binding( "3", "select(3)", "Toggle 3" ),
        Binding( "4", "select(4)", "Toggle 4" ),
        Binding( "5", "select(5)", "Toggle 5" ),
        Binding( "6", "select(6)", "Toggle 6" ),
        Binding( "7", "select(7)", "Toggle 7" ),
        Binding( "8", "select(8)", "Toggle 8" ),
        Binding( "9", "select(9)", "Toggle 9" ),
        Binding( "delete", "delete", "Delete current"),
        Binding( "a", "all(True)", "All on"),
        Binding( "ctrl+a", "all(False)", "All off"),
        Binding( "t", "toggle", "Toggle all"),
    ]

    CSS = """
    Screen > Horizontal > * {
        border: panel $primary;
    }
    """

    def compose( self ) -> ComposeResult:
        yield Header()
        with Horizontal():
            yield SelectionList[int](*[
                ( f"[red]S[/][green]e[/][yellow]l[/]ection [blue]{n}[/]", n ) for n in range( 50 )
            ])
            with VerticalScroll():
                yield Pretty([])
            yield TextLog()
        yield Footer()

    @on( OptionList.OptionHighlighted )
    @on( OptionList.OptionSelected )
    @on( SelectionList.SelectionHighlighted )
    @on( SelectionList.SelectionToggled )
    @on( SelectionList.SelectedChanged )
    def message_reporter(
            self,
            event: OptionList.OptionHighlighted |
            OptionList.OptionSelected |
            SelectionList.SelectionHighlighted |
            SelectionList.SelectionToggled |
            SelectionList.SelectedChanged
    ) -> None:
        self.query_one( TextLog ).write( f"{event!r}" )
        assert isinstance( event.control, SelectionList )
        self.query_one( Pretty ).update( event.control.selected )

    def action_select( self, n: int ) -> None:
        self.query_one( SelectionList ).toggle( n )

    def action_delete( self ) -> None:
        sl = self.query_one( SelectionList )
        if sl.highlighted is not None:
            sl.remove_option_at_index( sl.highlighted )

    def action_all( self, on: bool ) -> None:
        if on:
            self.query_one( SelectionList ).select_all()
        else:
            self.query_one( SelectionList ).deselect_all()

    def action_toggle( self ) -> None:
        self.query_one( SelectionList ).toggle_all()

if __name__ == "__main__":
    SelectionListtestApp().run()
