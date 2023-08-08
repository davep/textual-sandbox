from textual.app import App, ComposeResult
from textual.widgets import Tabs

class StyleTabsApp(App[None]):

    CSS = """
    Tabs .underline--bar {
        color: red;
        background: yellow;
    }
    """

    def compose(self) -> ComposeResult:
        yield Tabs("Mal", "Zoe", "Wash", "Inara", "Simon", "River", "Book", "Jayne")

if __name__ == "__main__":
    StyleTabsApp().run()
