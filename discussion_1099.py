from typing import cast
from dataclasses import dataclass

from rich.console import RenderableType
from rich.style import Style
from rich.text import Text
from textual.app import App, ComposeResult
from textual.binding import Binding
from textual.reactive import reactive, watch
from textual.screen import Screen
from textual.widget import Widget
from textual.widgets import Static, Footer


@dataclass
class State:
    msg: str = "Hello!"
    style: Style = Style(color = "red")

    def __rich__(self):
        return self.msg

class DisplayWidget(Widget):

    def state_changed(self, _):
        self.refresh()

    def on_mount(self):
        watch(self.app, "state", self.state_changed)

    def render(self) -> RenderableType:
        return Text(self.app.state.msg, style=self.app.state.style)


class ScreenA(Screen):
    def compose(self) -> ComposeResult:
        yield Static(Text("A"))
        yield DisplayWidget()
        yield Footer()

class ScreenB(Screen):
    def compose(self) -> ComposeResult:
        yield Static(Text("B"))
        yield DisplayWidget()
        yield Footer()


class StateApp(App[None]):
    state = reactive(State)

    SCREENS = {
        "a": ScreenA(),
        "b": ScreenB()
    }

    BINDINGS = [
        Binding("a", "switch_screen('a')", "Screen A",),
        Binding("b", "switch_screen('b')", "Screen B",),
        Binding("s", "change_state", "Change State"),
    ]

    def action_change_state(self) -> None:
        self.state = State(msg = self.state.msg.swapcase(), style=Style(underline=not self.state.style.underline))
        self.log(f"{self.state}")

    def on_mount(self) -> None:
        self.switch_screen("a")

if __name__ == "__main__":
    StateApp().run()

