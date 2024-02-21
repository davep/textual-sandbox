"""https://github.com/Textualize/textual/issues/3633"""

from textual.app import App, ComposeResult
from textual.widgets import Log


class CommandPaletteIsolation(App[None]):

    def compose(self) -> ComposeResult:
        yield Log()

    def tick(self) -> None:
        self.query_one(Log).write_line("Tick")

    def on_mount(self) -> None:
        self.set_interval(1, self.tick)


if __name__ == "__main__":
    CommandPaletteIsolation().run()

### command_palette_isolation.py ends here
