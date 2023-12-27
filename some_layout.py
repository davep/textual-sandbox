"""Layout example for a question on Discord."""

from textual.app import App, ComposeResult
from textual.containers import Horizontal, Vertical
from textual.widgets import Placeholder

class SomeLayoutApp(App[None]):

    CSS = """
    Placeholder {
        height: 1fr;
        width: 1fr;
    }

    #left-column {
        width: 3fr;
    }

    #main {
        width: 8fr;
    }
    """

    def compose(self) -> ComposeResult:
        with Horizontal():
            with Vertical(id="left-column"):
                yield Placeholder()
                yield Placeholder()
                yield Placeholder()
            with Vertical(id="main"):
                yield Placeholder()
                with Horizontal(id="central-belt"):
                    yield Placeholder()
                    yield Placeholder()
                    yield Placeholder()
                yield Placeholder()

if __name__ == "__main__":
    SomeLayoutApp().run()

### some_layout.py ends here
