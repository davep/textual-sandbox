from textual import on
from textual.app import App, ComposeResult
from textual.widgets import Button

class LogLocationApp(App[None]):

    def compose(self) -> ComposeResult:
        yield Button("Print", id="print")
        yield Button("Log", id="log")

    @on(Button.Pressed, "#print")
    def print_to_console(self) -> None:
        print("This was from a print")

    @on(Button.Pressed, "#log")
    def log_to_console(self) -> None:
        self.log.debug("This was from a log")

if __name__ == "__main__":
    LogLocationApp().run()
