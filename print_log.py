"""https://github.com/Textualize/textual/discussions/4004"""

from datetime import datetime

from textual.app import App, ComposeResult
from textual.events import Print
from textual.widgets import Log

class PrintLog(Log):

    def on_mount(self) -> None:
        self.begin_capture_print()

    def on_print(self, event: Print) -> None:
        self.write(event.text)

class PrintLogApp(App[None]):

    def compose(self) -> ComposeResult:
        yield PrintLog()

    def print_time(self) -> None:
        print(str(datetime.now()))

    def on_mount(self) -> None:
        self.set_interval(1.0, self.print_time)

if __name__ == "__main__":
    PrintLogApp().run()

### print_log.py ends here
