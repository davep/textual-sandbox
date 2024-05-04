"""Example of delaying work to allow an effect to happen.

https://github.com/Textualize/textual/issues/4364
"""

from textual import on
from textual.app import App, ComposeResult
from textual.widgets import Label, ListItem, ListView


class ListViewMenuApp(App[None]):
    def compose(self) -> ComposeResult:
        yield ListView(
            ListItem(Label("Beep"), id="beep"), ListItem(Label("Close"), id="close")
        )

    @on(ListView.Selected, item="#beep")
    def do_beep(self) -> None:
        self.bell()

    @on(ListView.Selected, item="#close")
    def do_close(self) -> None:
        self.call_after_refresh(self.exit)


if __name__ == "__main__":
    ListViewMenuApp().run()

### list_view_thing.py ends here
