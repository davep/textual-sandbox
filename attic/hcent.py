from textual.app import App, ComposeResult
from textual.widgets import Button, Label
from textual.containers import Horizontal

class CenteredApp(App):
    CSS = """
    Screen {
        align: center middle;
    }

    Horizontal {
        align: center middle;
        height: auto;
    }
    """

    def compose(self) -> ComposeResult:
        yield Horizontal(Label("I would like both this text and the button to be centered"))
        yield Horizontal(Button("PUSH ME!"))


if __name__ == "__main__":
    CenteredApp().run()

