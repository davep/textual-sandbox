"""https://github.com/Textualize/textual/issues/3562"""

from textual.app import App, ComposeResult
from textual.widgets import Collapsible, Label


class CollapsibleExampleApp(App[None]):

    CSS = """
    Collapsible > Contents {
        padding-left: 0;
    }
    """

    def compose(self) -> ComposeResult:
        with Collapsible():
            for n in range(10):
                yield Label(f"This is collapsed item {n}")


if __name__ == "__main__":
    CollapsibleExampleApp().run()

### collapsible_indent.py ends here
