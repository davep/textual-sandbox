"""https://github.com/Textualize/textual/discussions/1928"""

from pathlib import Path
from typing  import Any

from textual.app     import App, ComposeResult
from textual.widgets import Header, Footer, ListView, ListItem, Label

class FSEntry( ListItem ):

    def __init__( self, entry: Path ) -> None:
        super().__init__()
        self.entry = entry

    def compose( self ) -> ComposeResult:
        yield Label(
            self.entry.stem + ( "/" if self.entry.is_dir() else "" )
        )


class FSBrowser( ListView ):

    def __init__( self, cwd: Path | None = None, *args: Any, **kwargs: Any ) -> None:
        super().__init__( *args, **kwargs )
        self._cwd = ( cwd if cwd is not None else Path( "." ) ).resolve()

    def on_mount( self ) -> None:
        self._refresh()

    def _refresh( self ) -> None:
        # Clear out anything that's in here right now.
        self.clear()
        # Now populate with the content of the current working directory. We
        # want to be able to go up, so let's make sure there's an entry for
        # that...
        self.append( FSEntry( Path( ".." ) ) )
        # ...and then add everything else we find in the directory.
        for entry in self._cwd.iterdir():
            self.append( FSEntry( entry ) )

    def on_list_view_selected( self, event: ListView.Selected ) -> None:
        # If the user selected a directory entry...
        if event.item.entry.is_dir():
            # ...repopulate with its content.
            self._cwd = event.item.entry
            self._refresh()
        else:
            # If it's not a directory then it's a file or some sort of
            # file-like entry in the filesystem; handling of that would
            # happen here.
            pass


class FSBrowserApp( App[ None ] ):

    def compose( self ) -> ComposeResult:
        yield Header()
        yield FSBrowser()
        yield Footer()

if __name__ == "__main__":
    FSBrowserApp().run()
