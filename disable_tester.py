from textual.app        import App, ComposeResult
from textual.containers import Horizontal, Vertical, Grid
from textual.widgets    import Header, Footer, Input, Button, Tree, DataTable

try:
    from textual.widgets import Switch
except ImportError:
    from textual.widgets import Checkbox as Switch

class DisableTestingApp( App[ None ] ):

    CSS = """
    Horizontal {
        height: auto;
        border-bottom: solid red;
    }

    Horizontal > Button {
        width: 1fr;
        margin-left: 1;
        margin-right: 1;
    }

    Grid {
        grid-size: 2 6;
    }

    Grid > Button {
        width: 100%;
        height: 100%;
    }

    #inputs {
        height: auto;
    }

    *:disabled {
        border: solid red;
    }

    *:enabled {
        border: solid green;
    }
    """

    @property
    def tree( self ) -> Tree:
        tree = Tree( label="This is a test tree" )
        for n in range( 10 ):
            node = tree.root.add( f"Branch {n}" )
            for m in range( 10 ):
                node.add_leaf( f"Leaf {m} of branch {n}" )
        return tree

    @property
    def data_table( self ) -> DataTable:
        data_table = DataTable()
        data_table.add_columns( "Column 1", "Column 2", "Column 3", "Column 4" )
        data_table.add_rows(
            [ ( str( n ), str( n * 10 ), str( n * 100 ), str( n * 1000 ) ) for n in range( 100 ) ]
        )
        return data_table

    def compose( self ) -> ComposeResult:
        yield Header()
        yield Vertical(
            Horizontal(
                Button( "Disable", id="disable" ),
                Button( "Enable", id="enable" )
            ),
            Grid(
                Button( "Default Button" ),
                Button( "Primary Button", variant="primary" ),
                Button( "Success Button", variant="success" ),
                Button( "Warning Button", variant="warning" ),
                Button( "Error Button", variant="error" ),
                Vertical(
                    Input( "", placeholder="Empty Input" ),
                    Input( "Filled Input", placeholder="Filled Input" ),
                    id="inputs"
                ),
                self.tree,
                self.data_table,
                Switch()
            )
        )
        yield Footer()

    def on_button_pressed( self, event: Button.Pressed ) -> None:
        # Eventually this will be able to just set enabled/disabled on the
        # container and all the children will follow. For now though, as we
        # work through this, we'll do each child in turn.
        if event.button.id in ( "enable", "disable" ):
            for child in self.query( "Grid *" ):
                if hasattr( child, "disabled" ):
                    self.log.debug( f"Child {child} can be disabled" )
                    child.disabled = event.button.id == "disable"
                else:
                    self.log.debug( f"Child {child} CAN NOT BE disabled" )

if __name__ == "__main__":
    DisableTestingApp().run()

### disable_tester.py ends here
