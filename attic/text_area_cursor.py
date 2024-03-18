"""https://github.com/Textualize/textual/issues/4109"""

from textual.app import App, ComposeResult
from textual.widgets import Input, TextArea


class TextAreaCursorApp(App[None]):
    def compose(self) -> ComposeResult:
        yield Input()
        yield TextArea()


if __name__ == "__main__":
    TextAreaCursorApp().run()

### text_area_cursor.py ends here
