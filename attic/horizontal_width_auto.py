"""https://github.com/Textualize/textual/issues/4024"""

from textual.app import App, ComposeResult
from textual.containers import Horizontal
from textual.widgets import Button, Label


class HorizontalWidthAutoApp(App[None]):
    CSS = """
    Horizontal {
        border: solid red;
        height: auto;

        &.auto {
            width: auto;
        }

        Button, Label {
            margin-left: 1;
        }
    }
    """

    def compose(self) -> ComposeResult:
        with Horizontal(classes="auto"):
            for n in range(10):
                yield Button(f"{n} This is a very wide button {n}")
        with Horizontal():
            for n in range(10):
                yield Button(f"{n} This is a very wide button {n}")
        with Horizontal(classes="auto"):
            for n in range(10):
                yield Label(f"{n} This is a very wide label {n}")
        with Horizontal():
            for n in range(10):
                yield Label(f"{n} This is a very wide label {n}")


if __name__ == "__main__":
    HorizontalWidthAutoApp().run()

### horizontal_width_auto.py ends here
