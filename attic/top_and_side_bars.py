from textual.app import App, ComposeResult
from textual.containers import Horizontal, Vertical
from textual.widgets import Label

class TopAndSideBarApp(App[None]):

    CSS = """
    #side-bar {
        background: green;
        width: auto;
    }

    #top-bar {
        dock: top;
        background: red;
        height: auto;
    }
    """

    def compose(self) -> ComposeResult:
        with Horizontal():
            with Vertical(id="side-bar"):
                yield Label("Here's the side bar")
            with Vertical(id="main"):
                with Horizontal(id="top-bar"):
                    yield Label("Here's the top bar")
                yield Label("Here's the main body")

if __name__ == "__main__":
    TopAndSideBarApp().run()
