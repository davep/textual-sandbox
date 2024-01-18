"""Example of styling the underline in Tabs."""

from textual.app import App, ComposeResult
from textual.widgets import Tabs

class TabsColourApp(App[None]):

    CSS = """
    Underline > .underline--bar {
        color: red;
    }
    """

    def compose(self) -> ComposeResult:
        yield Tabs("Mal", "Jayne", "Kaylee", "Inara", "Zoe", "Wash", "River", "Simon")

if __name__ == "__main__":
    TabsColourApp().run()

### tab_underline.py ends here
