from textual.app import App, ComposeResult
from textual.widgets import Input, TextArea, Static, Button


class InputVsTextArea(App[None]):

    CSS = """
    Screen > *, Screen > *:focus {
        width: 50%;
        height: 1fr;
        border: solid red;
    }
    """

    def compose(self) -> ComposeResult:
        yield Input()
        yield TextArea()
        yield Static()
        yield Button()


if __name__ == "__main__":
    InputVsTextArea().run()

### input_vs_textarea.py ends here
