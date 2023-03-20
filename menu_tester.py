from __future__ import annotations

from random import randint

from rich.panel           import Panel
from rich.table           import Table
from rich.console         import RenderableType

from textual.app          import App, ComposeResult
from textual.widgets      import Header, Footer, Menu, TextLog
from textual.widgets.menu import MenuOption
from textual.containers   import Horizontal, Vertical

class MenuTestApp( App[ None ] ):

    CSS = """
    Horizontal {
        height: 1fr;
    }

    TextLog {
        height: 1fr;
        width: 1fr;
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

    def test_table( self, n: int ) -> Table:
        table = Table(title=f"Star Wars Movies Example {n}")
        table.add_column("Released", justify="right", style="cyan", no_wrap=True)
        table.add_column("Title", style="magenta")
        table.add_column("Box Office", justify="right", style="green")
        table.add_row("Dec 20, 2019", "Star Wars: The Rise of Skywalker", "$952,110,690")
        table.add_row("May 25, 2018", "Solo: A Star Wars Story", "$393,151,347")
        table.add_row("Dec 15, 2017", "Star Wars Ep. V111: The Last Jedi", "$1,332,539,889")
        table.add_row("Dec 16, 2016", "Rogue One: A Star Wars Story", "$1,332,439,889")
        return table

    @property
    def random_heights( self ) -> list[ RenderableType]:
        options: list[ RenderableType ] = []

        for n in range( 1_000 ):
            prompt_type = randint( 0, 4 )
            if prompt_type == 0:
                options.append( f"This is a single line prompt {n}" )
            elif prompt_type == 1:
                options.append( f"This is a two line prompt\nSee? This is the second line. {n}" )
            elif prompt_type == 2:
                options.append( self.test_table( n ) )
            elif prompt_type == 3:
                options.append( Panel( f"This is a panel.\n\nIt has multiple lines.", title=f"Option {n}" ) )
            else:
                options.append( f"{n} Yeah, I don't know what happened either" )
        return options

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
            with Horizontal():
                yield Menu[None](
                    *[ Panel( f"This is option {n}\nIt has multiple lines\n\n\n\nSee?") for n in range(1_000) ]
                )
                yield Menu[None](
                    *[ self.test_table( n ) for n in range(1_000) ]
                )
            with Horizontal():
                yield Menu[None]( *self.random_heights )
                yield TextLog()
        yield Footer()

    def on_menu_debug( self, event: Menu.Debug ):
        self.query_one( TextLog ).write( f"{event.cargo!r}" )

    def on_menu_option_highlighted( self, event: Menu.OptionHighlighted ) -> None:
        self.query_one( TextLog ).write( f"{event!r}" )

    def on_menu_option_selected( self, event: Menu.OptionSelected ) -> None:
        self.query_one( TextLog ).write( f"{event!r}" )

if __name__ == "__main__":
    MenuTestApp().run()
