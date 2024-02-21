"""https://github.com/Textualize/textual/issues/1661"""

from textual.app import App, ComposeResult
from textual.containers import Vertical
from textual.screen import Screen
from textual.widgets import Header, Footer, TextLog, Button
from textual.events import Paste
from textual.binding import Binding


class PasteButton(Button):

    def on_paste(self, event: Paste) -> None:
        self.app.query_one(TextLog).write(f"Button: {event}")


class PasteVertical(Vertical):

    def compose(self) -> ComposeResult:
        """Compose the child widgets."""
        yield PasteButton("This can get focus")

    def on_paste(self, event: Paste) -> None:
        self.app.query_one(TextLog).write(f"Vertical: {event}")


class PasteTextLog(TextLog):

    def on_paste(self, event: Paste) -> None:
        self.app.query_one(TextLog).write(f"TextLog: {event}")


class PasteScreen(Screen):

    def on_paste(self, event: Paste) -> None:
        self.query_one(TextLog).write(f"Screen: {event}")

    def compose(self) -> ComposeResult:
        yield Header()
        yield PasteVertical()
        yield PasteTextLog()
        yield Footer()


class PasteExplorer(App[None]):

    BINDINGS = [
        Binding("c", "clear", "Clear Log"),
    ]

    SCREENS = {"main": PasteScreen}

    CSS = """
    *:focus {
        border: double green;
    }

    Vertical {
        height: 1fr;
        border: round yellow;
    }

    TextLog {
        height: 80%;
        border: round red;
    }
    """

    def on_paste(self, event: Paste) -> None:
        self.query_one(TextLog).write(f"App: {event}")

    def on_mount(self) -> None:
        self.push_screen("main")

    def action_clear(self) -> None:
        """Clear"""
        self.query_one(TextLog).clear()


if __name__ == "__main__":
    PasteExplorer().run()

### paste_explorer.py ends here
