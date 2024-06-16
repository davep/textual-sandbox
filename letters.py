"""Example for a question on Discord."""

from textual.app import App, ComposeResult
from textual.containers import Horizontal
from textual.events import Key
from textual.widgets import Label


class Thing(Label):
    DEFAULT_CSS = """
    Thing {
        border: solid red;
        padding: 1 2;

        &.activated {
            border: double green;
        }
    }
    """


class ThingHolder(Horizontal, can_focus=True):
    KEYS = "abcdefg"

    def compose(self) -> ComposeResult:
        for key in self.KEYS:
            yield Thing(key, id=f"thing-{key}")

    def on_key(self, event: Key) -> None:
        if event.character and event.character in self.KEYS:
            self.query_one(f"#thing-{event.character}").set_class(True, "activated")


class LettersApp(App[None]):
    def compose(self) -> ComposeResult:
        yield ThingHolder()


if __name__ == "__main__":
    LettersApp().run()

### letters.py ends here
