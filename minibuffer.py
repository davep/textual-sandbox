from itertools import cycle

from textual.app import App, ComposeResult
from textual.containers import Grid
from textual.widgets import Label

from textual._command_palette import CommandPalette

class MinibufferApp(App[None]):

    CSS = """
    Grid {
        grid-size: 10;
    }

    Label {
        width: 1fr;
        height: 1fr;
        content-align: center middle;
    }

    Label.colour-0 {
        background: #881177;
    }

    Label.colour-1 {
        background: #aa3355;
    }

    Label.colour-2 {
        background: #cc6666;
    }

    Label.colour-3 {
        background: #ee9944;
    }

    Label.colour-4 {
        background: #eedd00;
    }

    Label.colour-5 {
        background: #99dd55;
    }

    Label.colour-6 {
        background: #44dd88;
    }

    Label.colour-7 {
        background: #22ccbb;
    }

    Label.colour-8 {
        background: #00bbcc;
    }

    Label.colour-9 {
        background: #0099cc;
    }

    Label.colour-10 {
        background: #3366bb;
    }

    Label.colour-11 {
        background: #663399;
    }
    """

    BINDINGS = [
        ("ctrl+p", "minibuffer"),
    ]

    def compose(self) -> ComposeResult:
        with Grid():
            colours = cycle(range(12))
            for _ in range(10 * 10):
                yield Label("It's a minibuffer!", classes=f"colour-{next(colours)}")

    def cycle_background(self) -> None:
        for label in self.query(Label):
            _, number = list(label.classes)[0].split("-")
            label.classes = f"colour-{(int(number)+1) % 12}"

    def on_mount(self) -> None:
        self.app.set_interval(0.5, self.cycle_background)

    def action_minibuffer(self) -> None:
        self.push_screen(CommandPalette())

if __name__ == "__main__":
    MinibufferApp().run()
