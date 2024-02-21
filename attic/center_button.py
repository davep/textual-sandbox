from textual.app import App, ComposeResult
from textual.widgets import Button


class ButtonApp(App[None]):

    CSS = """
    Screen {
        align: center middle;
    }
    """

    def compose(self) -> ComposeResult:
        yield Button("PUSH ME!")


if __name__ == "__main__":
    ButtonApp().run()
