"""https://github.com/Textualize/textual/discussions/3258"""

from textual.app import App, ComposeResult
from textual.binding import Binding
from textual.widgets import Label


class QuitApp(App[None]):

    BINDINGS = [
        Binding("ctrl+q", "quit"),
        Binding("ctrl+c", "do_not_quit"),
    ]

    def compose(self) -> ComposeResult:
        yield Label("Press Ctrl+Q to quit, don't press Ctrl+C!")

    def action_do_not_quit(self) -> None:
        pass


if __name__ == "__main__":
    QuitApp().run()
