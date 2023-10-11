"""https://github.com/Textualize/textual/discussions/3505"""

from textual.app import App, ComposeResult
from textual.events import Print
from textual.widgets import Log

class PrintingApp(App[None]):

    def compose(self) -> ComposeResult:
        yield Log()

    def on_print(self, event: Print) -> None:
        self.query_one(Log).write(event.text)

    def on_mount(self) -> None:
        self.begin_capture_print(self)
        print("Your message here")
        print("Your message here 2")

if __name__ == "__main__":
    PrintingApp().run()

### print_example.py ends here
