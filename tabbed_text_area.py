"""Example for TextArea cursor bug.

https://github.com/Textualize/textual/issues/4434
"""

from textual.app import App, ComposeResult
from textual.widgets import TabbedContent, TabPane, TextArea


class TabbedTextAreaApp(App[None]):
    def compose(self) -> ComposeResult:
        with TabbedContent():
            for tab in ("one", "two", "three", "four"):
                with TabPane(f"{tab}.py"):
                    for _ in range(3):
                        yield TextArea(language="python")


if __name__ == "__main__":
    TabbedTextAreaApp().run()

### tabbed_text_area.py ends here
