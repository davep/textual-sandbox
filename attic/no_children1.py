from textual.app import App, ComposeResult
from textual.widgets import Static

class NoChildren1(App[None]):

    def compose(self) -> ComposeResult:
        with Static():
            yield Static("Hello")

if __name__ == "__main__":
    NoChildren1().run()
