"""Layout example for a question on Discord."""

from textual.app import App, ComposeResult
from textual.containers import Horizontal, Vertical
from textual.widgets import Placeholder

class LeftColumn(Vertical):

    def compose(self) -> ComposeResult:
        yield Placeholder()
        yield Placeholder()
        yield Placeholder()

class MainData(Vertical):

    def compose(self) -> ComposeResult:
        yield Placeholder()
        with Horizontal():
            yield Placeholder()
            yield Placeholder()
            yield Placeholder()
        yield Placeholder()

class SomeLayoutApp(App[None]):

    CSS = """
    Placeholder {
        height: 1fr;
        width: 1fr;
    }

    LeftColumn {
        width: 3fr;
    }

    MainData {
        width: 8fr;
    }
    """

    def compose(self) -> ComposeResult:
        with Horizontal():
            yield LeftColumn()
            yield MainData()

if __name__ == "__main__":
    SomeLayoutApp().run()

### some_layout.py ends here
