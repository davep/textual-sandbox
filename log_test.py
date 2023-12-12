"""Show that Log works fine in dark and light mode."""

from textual.app import App, ComposeResult
from textual.widgets import Log

class LogApp(App[None]):

    BINDINGS = [
        ("d", "toggle_dark"),
    ]

    def compose(self) -> ComposeResult:
        yield Log()

    def on_mount(self) -> None:
        self.query_one(Log).write_lines((
            "This is line 0",
            "This is line 1",
            "This is line many"
        ))

if __name__ == "__main__":
    LogApp().run()

### log_test.py ends here
