from __future__ import annotations

from random import randint

from rich.panel           import Panel
from rich.table           import Table
from rich.console         import RenderableType

from textual.app          import App, ComposeResult
from textual.widgets      import Header, Footer, Menu, TextLog
from textual.widgets.menu import MenuOption
from textual.containers   import Horizontal, Vertical
from textual.widgets.menu import MenuSeparator

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

    BINDINGS = [
        ( "space", "add(-1)", "Add a random option" ),
        *[ ( str( n ), f"add({n})", f"Add option type {n}") for n in range(1,6)],
        ("c", "clear", "Clear"),
        ("d", "disable(True)", "Disable"),
        ("e", "disable(False)", "Enable"),
        ("f1","id_toggle_test", "Toggle")
    ]


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

    def type_of_option( self, n: int, option_type: int ) -> RenderableType | MenuSeparator:
        if option_type == 0:
            return f"This is a single line prompt {n}"
        elif option_type == 1:
            return f"This is a two line prompt\nSee? This is the second line. {n}"
        elif option_type == 2:
            return self.test_table( n )
        elif option_type == 3:
            return Panel( f"This is a panel.\n\nIt has multiple lines.", title=f"Option {n}" )
        elif option_type == 4:
            return MenuSeparator()
        return f"{n} Yeah, I don't know what happened either"

    @property
    def random_heights( self ) -> list[ RenderableType ]:
        return [
            self.type_of_option( n, randint( 0, 5 ) ) for n in range( 1_000 )
        ]

    def compose( self ) -> ComposeResult:
        yield Header()
        with Vertical():
            with Horizontal():
                yield Menu(
                    *[ MenuOption(
                        f"This is option {n}", disabled=not bool( n % 3 ),
                        id=str( n )
                    ) for n in range(1_000) ],
                    id="first"
                )
                yield Menu(
                    *[ Panel( f"This is option {n}" ) for n in range(1_000) ]
                )
                yield Menu( id="adder" )
            with Horizontal():
                yield Menu(
                    *[ Panel( f"This is option {n}\nIt has multiple lines\n\n\n\nSee?") for n in range(1_000) ]
                )
                yield Menu(
                    *[ self.test_table( n ) for n in range(1_000) ]
                )
            with Horizontal():
                yield Menu( *self.random_heights )
                yield TextLog()
        yield Footer()

    def on_menu_debug( self, event: Menu.Debug ):
        self.query_one( TextLog ).write( f"{event.cargo!r}" )

    def on_menu_option_highlighted( self, event: Menu.OptionHighlighted ) -> None:
        self.query_one( TextLog ).write( f"{event!r}" )

    def on_menu_option_selected( self, event: Menu.OptionSelected ) -> None:
        self.query_one( TextLog ).write( f"{event!r}" )
        self.query_one( TextLog ).write( f"\tThat was option: {event.menu.get_option_at_index( event.option_index )}" )

    def action_add( self, add_type: int ):
        menu = self.query_one( "#adder", Menu )
        menu.add( self.type_of_option( menu.option_count, randint( 0, 5 ) if add_type == -1 else add_type ) )

    def action_clear( self ):
        self.query_one( "#adder", Menu ).clear()

    def action_disable( self, disable: bool ) -> None:
        assert isinstance(self.focused, Menu)
        if disable:
            self.focused.disable_option_at_index( self.focused.highlighted )
        else:
            self.focused.enable_option_at_index( self.focused.highlighted )

    def action_id_toggle_test( self ) -> None:
        first = self.query_one( "#first", Menu )
        if first.get_option("1").disabled:
            first.enable_option( "1" )
        else:
            first.disable_option( "1" )

if __name__ == "__main__":
    MenuTestApp().run()
