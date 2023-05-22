from textual            import on
from textual.app        import App, ComposeResult
from textual.containers import Horizontal
from textual.widgets    import Header, Footer, SelectionList, TextLog, OptionList

class SelectionListtestApp( App[ None ] ):

    def compose( self ) -> ComposeResult:
        yield Header()
        with Horizontal():
            yield SelectionList[int](*[
                ( f"Selection {n}", n ) for n in range( 50 )
            ])
            yield TextLog()
        yield Footer()

    @on( OptionList.OptionHighlighted )
    @on( OptionList.OptionSelected )
    def message_reporter( self, event: object ) -> None:
        self.query_one( TextLog ).write( f"{event!r}" )

if __name__ == "__main__":
    SelectionListtestApp().run()
