"""Example of easy tooltipping of widgets."""

from textual.app import App, ComposeResult
from textual.widget import Widget
from textual.widgets import Button


def tip(widget: Widget, tip: str) -> Widget:
    widget.tooltip = tip
    return widget


class TipApp(App[None]):
    def compose(self) -> ComposeResult:
        yield tip(Button("Button 1"), "Here is some cool help!")
        yield tip(Button("Button 2"), "Here is some cool help!")
        yield tip(Button("Button 3"), "Here is some cool help!")
        yield tip(Button("Button 4"), "Here is some cool help!")


if __name__ == "__main__":
    TipApp().run()

### tip.py ends here
