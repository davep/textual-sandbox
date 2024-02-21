"""https://github.com/Textualize/textual/issues/2711"""

from textual.app import App, ComposeResult
from textual.containers import Center
from textual.reactive import var
from textual.widgets import Label


class WindowsIntervalBugApp(App[None]):

    CSS = """
    Screen {
        align: center middle;
    }
    """

    counter: var[int] = var(0)

    def compose(self) -> ComposeResult:
        yield Center(Label())

    def watch_counter(self) -> None:
        self.query_one(Label).update(str(self.counter))

    def bump_counter(self) -> None:
        self.counter += 1

    def on_mount(self) -> None:
        self.set_interval(30, self.bump_counter)


if __name__ == "__main__":
    WindowsIntervalBugApp().run()

### windows_timer_bug.py ends here
