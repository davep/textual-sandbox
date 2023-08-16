from textual.app import App, ComposeResult
from textual.widgets import Button, Input

class AutoFocusTestApp(App[None]):

    AUTO_FOCUS = None

    def compose(self) -> ComposeResult:
        for _ in range(5):
            yield Input()
            yield Button("Hey!")

if __name__ == "__main__":
    AutoFocusTestApp().run()
