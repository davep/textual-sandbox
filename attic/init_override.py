"""https://github.com/Textualize/textual/issues/3878"""

from textual.app import App, ComposeResult
from textual.reactive import var
from textual.widgets import Label, Log

class SomeWidget(Label):

    test_1: var[int] = var(0)
    test_2: var[int] = var(0, init=False)

    def watch_test_1(self, was: int, into: int) -> None:
        self.screen.query_one(Log).write_line(f"test_1 {was} -> {into}")

    def watch_test_2(self, was: int, into: int) -> None:
        self.screen.query_one(Log).write_line(f"test_2 {was} -> {into}")

class InitOverrideApp(App[None]):

    def compose(self) -> ComposeResult:
        yield SomeWidget()
        yield Log()

    def on_mount(self) -> None:
        def gndn() -> None:
            return
        self.watch(self.query_one(SomeWidget), "test_2", gndn)

if __name__ == "__main__":
    InitOverrideApp().run()

### init_override.py ends here
