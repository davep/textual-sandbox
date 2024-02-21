"""Test harness for tooltip issues."""

from textual import on
from textual.app import App, ComposeResult
from textual.containers import Container, Grid, Horizontal, VerticalScroll
from textual.screen import ModalScreen
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


class PopupScreen(ModalScreen, GoodTipper):

    DEFAULT_CSS = """
    PopupScreen {
        align: center middle;
        Label {
            border: solid cornflowerblue;
            padding: 1 2 1 2;
        }
    }
    """

    BINDINGS = [
        ("escape", "dismiss"),
    ]

    def compose(self) -> ComposeResult:
        yield self.tip(Label("Press escape to make this go away again"))


class Buttonatron(Grid, GoodTipper, can_focus=True):

    DEFAULT_CSS = """
    Buttonatron {
        height: 1fr;
        grid-size: 5;
        grid-rows: 7;

        Button {
           width: 1fr;
           height: 1fr;
           margin: 0 1 1 1;
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


class VisibleToggle(Container, GoodTipper, can_focus=True):

    DEFAULT_CSS = """
    VisibleToggle {
        Label {
            width: 1fr;
            height: 1fr;
            border: solid yellow;
            color: $text;
            background: red;
            content-align: center middle;
        }
    }
    """

    BINDINGS = [("space", "toggle_label")]

    def compose(self) -> ComposeResult:
        yield self.tip(Label("Press space to toggle my visible attribute!"))

    def action_toggle_label(self) -> None:
        self.query_one(Label).visible = not self.query_one(Label).visible

class DisplayToggle(Container, GoodTipper, can_focus=True):

    DEFAULT_CSS = """
    DisplayToggle {
        Label {
            width: 1fr;
            height: 1fr;
            border: solid red;
            color: $text;
            background: yellow;
            content-align: center middle;
        }
    }
    """

    BINDINGS = [("space", "toggle_label")]

    def compose(self) -> ComposeResult:
        yield self.tip(Label("Press space to toggle my display attribute!"))

    def action_toggle_label(self) -> None:
        self.query_one(Label).styles.display = (
            "none" if self.query_one(Label).styles.display == "block" else "block"
        )


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
    Buttonatron, LabelsAllTheWayDown, VisibleToggle, DisplayToggle {
        border: blank;
        &:focus {
            border: thick green;
        }
    }
    """

    BINDINGS = [
        ("s", "screen"),
    ]

    def compose(self) -> ComposeResult:
        with Horizontal():
            yield Buttonatron()
            yield LabelsAllTheWayDown()
        with Horizontal():
            yield VisibleToggle()
            yield DisplayToggle()

    def action_screen(self) -> None:
        self.push_screen(PopupScreen())

if __name__ == "__main__":
    TooltipHellApp().run()

### tooltip_hell.py ends here
