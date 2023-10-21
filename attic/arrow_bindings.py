from textual.app import App, ComposeResult
from textual.widgets import Label, Footer

class ArrowBindingsApp(App[None]):

    BINDINGS = [
        ("up", "up", "This goes up"),
        ("down", "down", "This goes down"),
        ("left", "left", "This goes left"),
        ("right", "right", "This goes right"),
    ]

    def compose(self) -> ComposeResult:
        yield Label("This has some bindings")
        yield Footer()

if __name__ == "__main__":
    ArrowBindingsApp().run()

### arrow_bindings.py ends here
