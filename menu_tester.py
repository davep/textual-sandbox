from textual.app     import App, ComposeResult
from textual.widgets import Header, Footer, Menu

class MenuTestApp( App[ None ] ):

    CSS = """
    Screen {
        align: center middle;
    }
    Menu {
        width: 50%;
        height: 90%;
    }
    """

    def compose( self ) -> ComposeResult:
        yield Header()
        yield Menu[int]()
        yield Footer()

if __name__ == "__main__":
    MenuTestApp().run()
