from textual import on
from textual.app import App, ComposeResult
from textual.message import Message
from textual.widgets import Label, Log

class MessageLeakApp(App[None]):

    def compose(self) -> ComposeResult:
        yield Label("Use the command palette")
        self.message_log = Log()
        yield self.message_log

    @on(Message)
    def logger(self, event: Message) -> None:
        try:
            self.message_log.write_line(f"{event!r}")
        except:
            pass

if __name__ == "__main__":
    MessageLeakApp().run()

