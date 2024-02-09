from textual.app import App, ComposeResult
from textual.widgets import Label

class FocusableLabel(Label, can_focus=True):

    DEFAULT_CSS = """
    FocusableLabel:focus {
        background: red;
    }
    """

class FocusLableExampleApp(App[None]):

    def compose(self) -> ComposeResult:
        yield Label("This won't focus")
        yield FocusableLabel("This will focus")
        yield Label("Not this")
        yield FocusableLabel("Totally this though")
        yield Label("Nope, no focus")
        yield FocusableLabel("Oh hey look I have focus!")

if __name__ == "__main__":
    FocusLableExampleApp().run()

### focus_label.py ends here
