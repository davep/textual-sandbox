"""Example of setting the screen's background colour."""

from textual.app import App, ComposeResult
from textual.containers import Container

class AppRootApp(App[None]):

    CSS = """
    Screen {
        background: red;
    }

    Container {
        margin: 10 10;
        background: blue;
    }
    """

    def compose(self) -> ComposeResult:
        yield Container()

if __name__ == "__main__":
    AppRootApp().run()

### app_root.py ends here
