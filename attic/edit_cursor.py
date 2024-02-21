"""https://github.com/Textualize/textual/issues/3722"""

from textual.app import App, ComposeResult
from textual.events import Key
from textual.widgets import Input, TextArea


class TabbyTextArea(TextArea):

    DEFAULT_CSS = """
    TabbyTextArea {
        background: $boost;
        color: $text;
        padding: 0 2;
        border: tall $background;
    }

    TabbyTextArea:focus {
        border: tall $accent;
    }
    """

    def on_mount(self) -> None:
        self.show_line_numbers = False

    async def _on_key(self, event: Key) -> None:
        if event.key == "tab":
            event.prevent_default()
            self.screen.focus_next()


class CursorApp(App[None]):

    def compose(self) -> ComposeResult:
        for _ in range(5):
            yield Input()
            yield TabbyTextArea()


if __name__ == "__main__":
    CursorApp().run()

### edit_cursor.py ends here
