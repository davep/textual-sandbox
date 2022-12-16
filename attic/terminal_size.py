from textual.app import App, ComposeResult
from textual.widgets import Static

class SizeApp(App[None]):

    def compose(self) -> ComposeResult:
        yield Static(
            f"Width={self.console.width}, Height={self.console.height}"
        )

if __name__=="__main__":
    SizeApp().run()
