from textual.app import App, ComposeResult
from textual.widgets import TabbedContent, TabPane, Label, Tabs

class TCRenameApp(App[None]):

    BINDINGS = [
        ("space", "rename"),
    ]

    def compose(self) -> ComposeResult:
        with TabbedContent():
            with TabPane("One", id="one"):
                yield Label("Press space to change my Tab's label")
            with TabPane("Two", id="two"):
                yield Label("This one won't rename")

    def action_rename(self) -> None:
        tabbed_content = self.query_one(TabbedContent)
        tabbed_content.get_tab("one").update("Renamed!")
        tabbed_content.query_one(Tabs).show("one")

if __name__ == "__main__":
    TCRenameApp().run()

### content_tab_relabel.py ends here
