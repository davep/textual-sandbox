"""Example of a problem with the loading property."""

from textual.app import App, ComposeResult
from textual.widgets import Static, Label, Footer, Button

class Fixed(Label):

    DEFAULT_CSS = """
    Fixed {
        width: 1fr;
        height: 10;
        background: teal;
    }
    """

class LabelLoadingTestApp(App[None]):

    BINDINGS = [
        ("space", "toggle", "Toggle the loading indicator"),
    ]

    def compose(self) -> ComposeResult:
        yield Label()
        yield Label("This is a test")
        yield Static()
        yield Static("This is a test")
        yield Footer()
        yield Button("")
        yield Button("Foo")
        yield Fixed("This is fixed")

    def action_toggle(self) -> None:
        for widget in self.query("Screen > *").results():
            widget.loading = not widget.loading

if __name__ == "__main__":
    LabelLoadingTestApp().run()

### label_loading.py ends here
