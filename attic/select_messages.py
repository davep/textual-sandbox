"""For https://github.com/Textualize/textual/discussions/3400#discussioncomment-7110127"""

from itertools import cycle

from textual import on
from textual.app import App, ComposeResult
from textual.widgets import Log, Select


class SelectMessagesApp(App[None]):

    def compose(self) -> ComposeResult:
        yield Select[int]((("One", 0), ("Two", 1)))
        yield Log()

    def on_mount(self) -> None:
        self.selections = cycle((0, 1, None))
        self.set_interval(0.25, self.change_value)

    @on(Select.Changed)
    def log_select(self, event: Select.Changed) -> None:
        self.query_one(Log).write_line(f"{event!r} -> {event.value!r}")

    def change_value(self) -> None:
        self.query_one(Select).value = next(self.selections)


if __name__ == "__main__":
    SelectMessagesApp().run()

### select_messages.py ends here
