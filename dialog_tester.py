from functools import partial
from itertools import cycle
from typing import get_args

from textual import on
from textual.app import App, ComposeResult
from textual.containers import Grid, Horizontal, Vertical
from textual.reactive import var
from textual.screen import ModalScreen
from textual.widgets import Button, Dialog, Label, Input, Select, OptionList, Checkbox
from textual.widgets.dialog import DialogVariant

class ModalDialog(ModalScreen):

    DEFAULT_CSS = """
    ModalDialog {
        align: center middle;
    }
    """

    BINDINGS = [
        ("escape", "pop_screen"),
    ]

    counter: var[int] = var(0)

    def bump(self) -> None:
        self.counter += 1

    def on_mount(self) -> None:
        try:
            if not self.query_one(Dialog).title:
                self.set_interval(1, self.bump)
        except:
            pass

    def _watch_counter(self) -> None:
        if self.is_mounted:
            self.query_one(Dialog).title = (
                f"This is a test dialog ({self.counter}) "
                f"{'=' * ((self.counter // 5) + 1)}"
            )


class BigDialog(ModalDialog):

    NAMES =[
        "Edison Carter",
        "Max Headroom",
        "Theora Jones",
        "Ben Cheviot",
        "Bryce Lynch",
        "Murray McKenzie",
        "Blank Reg",
        "Ned Grossberg"
    ]

    DEFAULT_CSS = """
    BigDialog ActionArea Input {
        width: 30;
    }
    """

    def compose(self) -> ComposeResult:
        with Dialog():
            for _ in range(10):
                yield Label("Hello, World!")
                yield Select[str]((name, name) for name in self.NAMES)
                yield Label("Hello, World!")
                yield OptionList(*self.NAMES)
            with Dialog.ActionArea():
                with Dialog.ActionArea.GroupLeft():
                    yield Label("Input:")
                    yield Input()
                    yield Checkbox("Checked?")
                yield Button("Yes")
                yield Button("No")
                yield Button("Cancel")
                yield Button("Guess")
                yield Button("Whatever")

class YesNo(ModalDialog):

    def __init__(self, question: str) -> None:
        super().__init__()
        self._question = question

    def compose(self) -> ComposeResult:
        with Dialog(title="Well?"):
            yield Label(self._question)
            with Dialog.ActionArea():
                yield Button("Yes")
                yield Button("No")

class YesNoCheckbox(ModalDialog):

    def __init__(self, question: str) -> None:
        super().__init__()
        self._question = question

    def compose(self) -> ComposeResult:
        with Dialog(title="Well?"):
            yield Label(self._question)
            with Dialog.ActionArea():
                with Dialog.ActionArea.GroupLeft():
                    yield Checkbox("Seriously though?")
                yield Button("Yes")
                yield Button("No")

class BadVariant(ModalDialog):

    def compose(self) -> ComposeResult:
        with Dialog(variant="Loki"):
            yield Label("I am burdened with glorious purpose!")

class SuccessDialog(ModalDialog):

    def compose(self) -> ComposeResult:
        with Dialog.success(title="It worked!"):
            yield Label("That thing we did worked!")
            with Dialog.ActionArea():
                yield Button("Woot!")
                yield Button("Yay!")
                yield Button("Awesome!")

class WarningDialog(ModalDialog):

    def compose(self) -> ComposeResult:
        with Dialog.warning(title="Be aware"):
            yield Label("Be aware of this thing you need to be aware of!")
            with Dialog.ActionArea():
                yield Button("Oh!")
                yield Button("Hmm")
                yield Button("Intensify anxiety")

class ErrorDialog(ModalDialog):

    def compose(self) -> ComposeResult:
        with Dialog.error(title="OH NOES BAD THINGS!"):
            yield Label("Bad things! Bad things are happening!")
            with Dialog.ActionArea():
                yield Button("Eeep!")
                yield Button("Run away!")
                yield Button("Yeah I think I will nope out!")

class UndecidedDialog(ModalDialog):

    def compose(self) -> ComposeResult:
        with Dialog(title="I can't decide what I am"):
            yield Label("What type of dialog shall I be today?!?!?")
            with Dialog.ActionArea():
                for variant in get_args(DialogVariant):
                    yield Button(variant.capitalize(), id=variant)

    def on_button_pressed(self, event: Button.Pressed) -> None:
        event.stop()
        assert isinstance(event.button.id, str)
        self.query_one(Dialog).variant = event.button.id

class ManyButtons(ModalDialog):

    def compose(self) -> ComposeResult:
        with Dialog():
            yield Label("Check out these buttons!")
            with Dialog.ActionArea():
                for n in range(5):
                    yield Button(f"This is button {str(n) * max(1, n)} oh yes it is")

class DialogDialog(ModalDialog):

    DEFAULT_CSS = """
    DialogDialog > Horizontal {
        align: center middle;
        width: 1fr;
        height: 1fr;
        visibility: hidden;

        &> Dialog {
            visibility: visible;
        }
    }
    """

    def compose(self) -> ComposeResult:
        with Horizontal():
            with Dialog(title="Left dialog"):
                yield Label("As you look at me, I'm on the left.")
                with Dialog.ActionArea():
                    yield Button("Okay")
            with Dialog(title="Right dialog"):
                yield Label("As you look at me, I'm on the right.")
                with Dialog.ActionArea():
                    yield Button("Okay")

class DialogTesterApp(App[None]):

    CSS = """
    Tooltip {
        max-width: 100%;
    }

    #_default {
        layers: background buttons;
        align: center middle;

        &> Vertical {
            width: auto;
            height: auto;
            visibility: hidden;
            &> * {
                visibility: visible;
            }
            Button {
                margin-bottom: 1;
                width: 50vw;
            }
        }
    }

    #_default Grid {
        layer: background;
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
        with Vertical():
            yield Button("Big Dialog", id="big")
            yield Button("Yes/No Dialog", id="yes-no")
            yield Button("Seriously Yes/No Dialog", id="seriously-yes-no")
            yield Button("Bad Variant", id="bad-variant")
            yield Button("Success Variant", id="success-variant")
            yield Button("Warning Variant", id="warning-variant")
            yield Button("Error Variant", id="error-variant")
            yield Button("Undecided Variant", id="undecided-variant")
            yield Button("Many Buttons", id="many-buttons")
            yield Button("Dialog Dialog", id="dialog-dialog")

    @on(Button.Pressed)
    def test(self, event: Button.Pressed) -> None:
        if event.button.id is not None:
            self.push_screen({
                "big": BigDialog,
                "yes-no": partial(YesNo, "Working?"),
                "seriously-yes-no": partial(YesNoCheckbox, "Working?"),
                "bad-variant": BadVariant,
                "success-variant": SuccessDialog,
                "warning-variant": WarningDialog,
                "error-variant": ErrorDialog,
                "undecided-variant": UndecidedDialog,
                "many-buttons": ManyButtons,
                "dialog-dialog": DialogDialog,
            }[event.button.id]())

if __name__ == "__main__":
    DialogTesterApp().run()
