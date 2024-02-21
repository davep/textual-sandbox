from textual.app import App, ComposeResult
from textual.widgets import Input


class DoubleCursorApp(App[None]):

    def compose(self) -> ComposeResult:
        yield Input()


if __name__ == "__main__":
    DoubleCursorApp().run()
