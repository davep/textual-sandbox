from textual.app import App, ComposeResult
from textual.widgets import TabbedContent, TabPane, Label

class DisableTabApp(App[None]):

    def compose(self) -> ComposeResult:
        with TabbedContent(id="top-level"):
            with TabPane("One", id="one", disabled=True):
                yield Label("This is tab one")
            with TabPane("Two", id="two"):
                yield Label("This is tab two")

if __name__ == "__main__":
    DisableTabApp().run()
