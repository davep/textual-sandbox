"""An example of using layers to fake a dialog with background refresh.

See https://github.com/Textualize/textual/issues/3055 -- this was to answer
a question relating to that was asked on Discord, giving this as an
alternative approach that might work depending on situation.
"""

from datetime import datetime

from textual.app import App, ComposeResult, RenderResult
from textual.containers import Grid, Vertical
from textual.widgets import Label, Button

class PopUp(Vertical):

    DEFAULT_CSS = """
    PopUp {
        align: center middle;
        background: $panel 50%;
        width: 30%;
        height: 30%;
        border: thick red;
    }
    """

    def on_mount(self) -> None:
        self.screen.set_focus(self.children[0])

    def compose(self) -> ComposeResult:
        yield Button("Press me to close me")

    def on_button_pressed(self) -> None:
        self.remove()

class Time(Label):

    DEFAULT_CSS = """
    Time {
        width: 1fr;
        height: 1fr;
        content-align: center middle;
        background: darkred;
        border: round red;
    }
    """

    def on_mount(self) -> None:
        self.auto_refresh = 0.2

    def render(self) -> RenderResult:
        return str(datetime.now())

class BackgroundRefreshApp(App[None]):

    CSS = """
    Screen {
        layers: popup;
        align: center middle;
    }

    Grid {
        grid-size: 6;
    }

    PopUp {
        layer: popup;
    }
    """

    BINDINGS = [
        ("enter", "popup"),
    ]

    def compose(self) -> ComposeResult:
        with Grid():
            for _ in range(36):
                yield Time()

    def action_popup(self) -> None:
        self.mount(PopUp())

if __name__ == "__main__":
    BackgroundRefreshApp().run()
