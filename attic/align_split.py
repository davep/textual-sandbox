from textual.app import App, ComposeResult
from textual.containers import Horizontal
from textual.widgets import Button, Checkbox


class AlignSplitApp(App[None]):

    CSS = """
    Horizontal.right {
        align-horizontal: right;
    }
    """

    def compose(self) -> ComposeResult:
        with Horizontal():
            with Horizontal(classes="left"):
                yield Button("Save")
                yield Button("Load")
            with Horizontal(classes="right"):
                yield Button("Start")
                yield Checkbox("Convert to mp3")


if __name__ == "__main__":
    AlignSplitApp().run()

### align_split.py ends here
