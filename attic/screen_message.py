"""https://discord.com/channels/1026214085173461072/1033754296224841768/1179723389091463208"""

from textual import on
from textual.app import App, ComposeResult
from textual.message import Message
from textual.screen import Screen
from textual.widgets import Button, Log

class Child(Screen[None]):

    class Done(Message):
        pass

    def compose(self) -> ComposeResult:
        yield Button("GTFO")

    @on(Button.Pressed)
    def gtfo(self) -> None:
        self.app.post_message(self.Done())
        self.dismiss(None)

class MessageOnTheWayOutApp(App[None]):

    def compose(self) -> ComposeResult:
        yield Button("Show child")
        yield Log()

    def screen_callback(self, _: None) -> None:
        self.query_one(Log).write_line("Callback")

    @on(Button.Pressed)
    def show_child(self) -> None:
        self.push_screen(Child(), callback=self.screen_callback)

    @on(Child.Done)
    def log_child_done(self) -> None:
        self.query_one(Log).write_line("Child.Done")


if __name__ == "__main__":
    MessageOnTheWayOutApp().run()

### screen_message.py ends here
