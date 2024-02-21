from textual.app import App, ComposeResult
from textual.widgets import Footer, Label


class NoCtrlCApp(App[None]):

    BINDINGS = [("ctrl+q", "quit"), ("ctrl+c", "gndn")]

    def compose(self) -> ComposeResult:
        yield Label("Press Ctrl+Q to quit")
        yield Footer()


if __name__ == "__main__":
    NoCtrlCApp().run()

### no-ctrl-c.py ends here
