"""https://github.com/Textualize/textual/issues/3291"""

from dataclasses import dataclass

from textual import on
from textual.app import App, ComposeResult
from textual.containers import Horizontal, Vertical
from textual.message import Message
from textual.screen import ModalScreen
from textual.widgets import Button, Log


class TestModal(ModalScreen[str]):

    DEFAULT_CSS = """
    TestModal {
        align: center middle
    }
    """

    def compose(self) -> ComposeResult:
        yield Button("Close and send message")

    @on(Button.Pressed)
    def close_and_send(self) -> None:
        self.dismiss("From the modal screen")


class TestWidget(Vertical):

    DEFAULT_CSS = """
    TestWidget Horizontal {
        align: center middle;
        height: auto;
    }

    TestWidget Horizontal > Button {
        margin: 0 4 0 4;
    }

    TestWidget Log {
        border: solid green;
    }
    """

    @dataclass
    class TestMessage(Message):
        came_from: str

    def compose(self) -> ComposeResult:
        with Horizontal():
            yield Button("Just send the message", id="send_now")
            yield Button("Open a modal screen", id="send_via_modal")
        yield Log()

    @on(Button.Pressed, "#send_now")
    def message_from_here(self) -> None:
        self.post_message(self.TestMessage("Directly from a post_message"))

    def modal_callback(self, calling_from: str) -> None:
        self.post_message(self.TestMessage(calling_from))

    @on(Button.Pressed, "#send_via_modal")
    def message_from_callback(self) -> None:
        self.app.push_screen(TestModal(), callback=self.modal_callback)


class CallbackBubbleIssueApp(App[None]):

    def compose(self) -> ComposeResult:
        yield TestWidget()

    @on(TestWidget.TestMessage)
    def log_message(self, event: TestWidget.TestMessage) -> None:
        self.query_one(Log).write_line(f"{event!r}")


if __name__ == "__main__":
    CallbackBubbleIssueApp().run()

### callback_message_bubble.py ends here
