from rich.panel           import Panel
from textual.app          import App, ComposeResult
from textual.widgets      import Header, Footer, Menu, TextLog
from textual.widgets.menu import MenuOption
from textual.containers   import Horizontal, Vertical

class MenuTestApp( App[ None ] ):

    CSS = """
    Horizontal {
        height: 2fr;
    }

    TextLog {
        height: 1fr;
        border: round blue;
    }

    Menu {
        border: round red;
        width: 1fr;
        height: 1fr;
    }

    *:focus {
        border: double green;
    }
    """

    def compose( self ) -> ComposeResult:
        yield Header()
        with Vertical():
            with Horizontal():
                yield Menu[int](
                    *[ MenuOption( f"This is option {n}", data=n) for n in range(1_000) ]
                )
                yield Menu[None](
                    *[ Panel( f"This is option {n}") for n in range(1_000) ]
                )
                yield Menu[None]()
            yield TextLog()
        yield Footer()

if __name__ == "__main__":
    MenuTestApp().run()
