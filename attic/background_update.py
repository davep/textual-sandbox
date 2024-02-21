"""https://github.com/Textualize/textual/issues/3055"""

from datetime import datetime

from textual.app import App, ComposeResult, RenderResult
from textual.containers import Grid, Vertical
from textual.screen import ModalScreen
from textual.widgets import Label, Button


class PopUp(ModalScreen[None]):

    DEFAULT_CSS = """
    PopUp {
        align: center middle;
    }

    PopUp Vertical {
        align: center middle;
        background: $panel 50%;
        width: 30%;
        height: 30%;
        border: thick red;
    }
    """

    def compose(self) -> ComposeResult:
        with Vertical():
            yield Button("Press me to close me")

    def on_button_pressed(self) -> None:
        self.dismiss()


class Time(Label):

    DEFAULT_CSS = """
    Time {
        width: 1fr;
        height: 1fr;
        content-align: center middle;
        background: darkred;
        border: round red;
    }

    Time.green {
        background: green;
    }
    """

    def swap_colour(self) -> None:
        self.toggle_class("green")

    def on_mount(self) -> None:
        self.auto_refresh = 0.2
        self.set_interval(1.0, self.swap_colour)

    def render(self) -> RenderResult:
        return str(datetime.now())


class BackgroundRefreshApp(App[None]):

    CSS = """
    Grid {
        grid-size: 6;
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
        self.push_screen(PopUp())


if __name__ == "__main__":
    BackgroundRefreshApp().run()
