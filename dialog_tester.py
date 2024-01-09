from functools import partial
from itertools import cycle

from textual.app import App, ComposeResult
from textual.containers import Grid
from textual.screen import ModalScreen, Screen
from textual.widgets import Button, Dialog, Label, Input, Select, OptionList

class DialogTest(ModalScreen):

    _NAMES =[
        "Edison Carter",
        "Max Headroom",
        "Theora Jones",
        "Ben Cheviot",
        "Bryce Lynch",
        "Murray McKenzie",
        "Blank Reg",
        "Ned Grossberg"
    ]

    NAMES = cycle(_NAMES)

    DEFAULT_CSS = """
    DialogTest {
        align: center middle;

        ActionArea Input {
            width: 30;
        }
    }
    """

    def compose(self) -> ComposeResult:
        with Dialog(title=next(self.NAMES)):
            for _ in range(10):
                yield Label("Hello, World!")
                yield Select[str]((name, name) for name in self._NAMES)
                yield Label("Hello, World!")
                yield OptionList(*self._NAMES)
            with Dialog.ActionArea():
                with Dialog.ActionArea.GroupLeft():
                    yield Label("Input:")
                    yield Input()
                yield Button("Yes")
                yield Button("No")
                yield Button("Cancel")
                yield Button("Guess")
                yield Button("Whatever")

    def new_title(self) -> None:
        self.query_one(Dialog).title = next(self.NAMES)

    def on_mount(self) -> None:
        self.set_interval(1, partial(self.new_title))

class DialogTesterApp(App[None]):

    CSS = """
    Grid {
        grid-size: 11;

        Label {
            width: 1fr;
            height: 1fr;
            content-align: center middle;
            transition: background 220ms linear;

            &.colour-0 {
                background: #881177;
            }

            &.colour-1 {
                background: #aa3355;
            }

            &.colour-2 {
                background: #cc6666;
            }

            &.colour-3 {
                background: #ee9944;
            }

            &.colour-4 {
                background: #eedd00;
            }

            &.colour-5 {
                background: #99dd55;
            }

            &.colour-6 {
                background: #44dd88;
            }

            &.colour-7 {
                background: #22ccbb;
            }

            &.colour-8 {
                background: #00bbcc;
            }

            &.colour-9 {
                background: #0099cc;
            }

            &.colour-10 {
                background: #3366bb;
            }

            &.colour-11 {
                background: #663399;
            }
        }
    }
    """

    def compose(self) -> ComposeResult:
        with Grid():
            colours = cycle(range(12))
            for _ in range(11 * 11):
                yield Label("Woot Dialog!", classes=f"colour-{next(colours)}")

    def on_mount(self) -> None:
        self.push_screen(DialogTest())

if __name__ == "__main__":
    DialogTesterApp().run()
