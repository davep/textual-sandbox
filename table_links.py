from textual.app        import App, ComposeResult
from textual.widgets    import Header, Footer, DataTable

class DTLinksApp( App[ None ] ):

    CSS = """
    DataTable {
        height: 1fr;
    }
    """

    def compose( self ) -> ComposeResult:
        yield Header()
        yield DataTable()
        yield Footer()

    def on_mount( self ) -> None:
        dt = self.query_one( DataTable )
        dt.focus()
        dt.add_columns( "Title", "URL Markup", "URL Markup With Label", "No Markup" )
        dt.add_rows( [ (
            f"Relevant XKCD {n}",
            f"[link]https://xkcd.com/{n}/[/]",
            f"[link=https://xkcd.com/{n}/]XKCD {n}[/]",
            f"https://xkcd.com/{n}/"
        ) for n in range( 500 ) ] )

if __name__ == "__main__":
    DTLinksApp().run()
