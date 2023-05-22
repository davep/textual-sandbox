from textual.app        import App, ComposeResult
from textual.containers import Horizontal
from textual.widgets    import Header, Footer, SelectionList, TextLog

class SelectionListtestApp( App[ None ] ):

    def compose( self ) -> ComposeResult:
        yield Header()
        with Horizontal():
            yield SelectionList[int](*[
                ( f"Selection {n}", n ) for n in range( 50 )
            ])
            yield TextLog()
        yield Footer()

if __name__ == "__main__":
    SelectionListtestApp().run()
