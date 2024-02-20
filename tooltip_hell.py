"""Test harness for tooltip issues."""

from textual import on
from textual.app import App, ComposeResult
from textual.containers import Grid, VerticalScroll
from textual.widget import Widget
from textual.widgets import Button, Label

class GoodTipper:

    @staticmethod
    def tip(widget: Widget) -> Widget:
        widget.tooltip = (
            f"[bold]This is a tooltip![/]\n\n"
            f"[italic]The widget's ID is {widget.id}\n\n"
            "It has a bunch of text. Cool huh?"
        )
        return widget

class Buttonatron(Grid, GoodTipper, can_focus=True):

    DEFAULT_CSS = """
    Buttonatron {
        height: 1fr;
        grid-size: 5;
        grid-rows: 5;

        Button {
           width: 1fr;
           height: 1fr;
           margin: 0 1 0 1;
        }
    }
    """

    BINDINGS = [("space", "add")]

    def action_add(self) -> None:
        button_id = str(len(self.children))
        self.mount(
            self.tip(
                Button(f"Button #{button_id}\n\nPress me to remove me", id=f"button-{button_id}")
            )
        )

    @on(Button.Pressed)
    def remove_button(self, event: Button.Pressed) -> None:
        event.control.remove()

class LabelsAllTheWayDown(VerticalScroll, GoodTipper, can_focus=True):

    DEFAULT_CSS = """
    LabelsAllTheWayDown {
        Grid {
            grid-size: 5;
            height: auto;
            grid-rows: 10;
            Label {
                background: $panel;
                border: panel cornflowerblue;
                width: 1fr;
                height: 1fr;
                margin-bottom: 1;
            }
        }
    }
    """

    def compose(self) -> ComposeResult:
        with Grid():
            for n in range(200):
                yield self.tip(Label(f"Here is label #{n}", id=f"label-{n}"))

class TooltipHellApp(App[None]):

    CSS = """
    Screen > * {
        border: blank;
        &:focus {
            border: thick green;
        }
    }
    """

    def compose(self) -> ComposeResult:
        yield Buttonatron()
        yield LabelsAllTheWayDown()

if __name__ == "__main__":
    TooltipHellApp().run()

### tooltip_hell.py ends here
