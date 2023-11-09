from textual.app import App, ComposeResult
from textual.widgets import Label, Header

class NoCommandPaletteButtonApp(App[None]):

    HEADER = "Hello, World!"

    def compose(self) -> ComposeResult:
        yield Header()
        yield Label("Hey look no command palette button!")

    def on_mount(self) -> None:
        self.query_one("HeaderIcon").visible = True

if __name__ == "__main__":
    NoCommandPaletteButtonApp().run()

### command_palette_button.py ends here
