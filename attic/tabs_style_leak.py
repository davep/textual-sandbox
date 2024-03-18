"""Example of TabbedContent leaking Tabs styling.

https://github.com/Textualize/textual/issues/4232
"""

from textual.app import App, ComposeResult
from textual.containers import Horizontal, Vertical
from textual.widgets import Button, Label, TabbedContent, TabPane, Tabs


class TabsStyleLeakApp(App[None]):
    CSS = """
    Vertical, TabbedContent {
        width: 1fr;
    }
    """

    def stuff(self) -> ComposeResult:
        yield Label("This label is topmost")
        yield Button("This button is second")
        yield Tabs("After", "Button")

    def compose(self) -> ComposeResult:
        with Horizontal():
            with Vertical():
                yield from self.stuff()
            with TabbedContent():
                with TabPane("Test"):
                    yield from self.stuff()


if __name__ == "__main__":
    TabsStyleLeakApp().run()

### tabs_style_leak.py ends here
