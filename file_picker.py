import os

from textual.app        import App, ComposeResult
from textual.containers import Horizontal
from textual.widgets    import Header, Footer, ListView, ListItem, TextLog, Label
from textual.reactive   import reactive

class FileReader( App[ None ] ):

    CSS = """
    ListView {
        width: 1fr;
    }
    TextLog {
        width: 1fr;
    }
    """

    files = reactive([])

    def compose( self ) -> ComposeResult:
        for file in os.listdir():
            if file[0] != ".":
                self.files.append(file)
        yield Header()
        yield Horizontal(
            ListView( *[
                ListItem( Label( f"{file}") , id=f"{file}" )
                for file in self.files
            ] ),
            TextLog()
        )
        yield Footer()

    def on_list_view_highlighted( self, event: ListView.Highlighted ) -> None:
        self.query_one( TextLog ).write( event )

    def on_list_view_selected( self, event: ListView.Selected ) -> None:
        self.query_one( TextLog ).write(event )

if __name__ == "__main__":
    FileReader().run()
