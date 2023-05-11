from textual.app                    import App, ComposeResult
from textual.containers             import Horizontal
from textual.widgets                import Header, Footer, SelectionList, TextLog
from textual.widgets.selection_list import Selection

class SelectionListtestApp( App[ None ] ):

    def compose( self ) -> ComposeResult:
        yield Header()
        with Horizontal():
            yield SelectionList[int](*[
                Selection( n, f"Selection {n}" ) for n in range( 50 )
            ])
            yield TextLog()
        yield Footer()

if __name__ == "__main__":
    SelectionListtestApp().run()
