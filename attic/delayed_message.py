"""https://github.com/Textualize/textual/issues/2750"""

from __future__ import annotations

from dataclasses import dataclass

from textual import on
from textual.app import App, ComposeResult
from textual.containers import Vertical, Horizontal
from textual.message import Message
from textual.widget import Widget
from textual.widgets import Button, TextLog


class MessageSource(Widget):

    @dataclass
    class Boop(Message):
        source: MessageSource

        def control(self) -> MessageSource:
            return self.source

    def send_now(self) -> None:
        self.post_message(self.Boop(self))

    def send_after_refresh(self) -> None:
        self.call_after_refresh(self.post_message, self.Boop(self))

    def indirect_sender(self):
        self.post_message(self.Boop(self))

    def send_indirectly_after_refresh(self) -> None:
        self.call_after_refresh(self.indirect_sender)


class ReportingContainer(Vertical):

    @on(MessageSource.Boop)
    def report(self) -> None:
        self.app.query_one(TextLog).write("Container got boop")


class DelayedMessageApp(App[None]):

    CSS = """
    Screen > Horizontal > * {
        width: 1fr;
    }

    #buttons {
        height: auto;
    }

    ReportingContainer {
        display: none;
    }
    """

    def compose(self) -> ComposeResult:
        with Horizontal(id="buttons"):
            yield Button("Send Now", id="now")
            yield Button("Send After Refresh", id="refresh")
            yield Button("Send Indirectly After Refresh", id="indirectly")
        with ReportingContainer():
            yield MessageSource()
        yield TextLog()

    @on(Button.Pressed, "#now")
    def send_now(self) -> None:
        self.query_one(TextLog).write("-" * 50)
        self.query_one(MessageSource).send_now()

    @on(Button.Pressed, "#refresh")
    def send_after_refresh(self) -> None:
        self.query_one(TextLog).write("-" * 50)
        self.query_one(MessageSource).send_after_refresh()

    @on(Button.Pressed, "#indirectly")
    def send_indirectly_after_refresh(self) -> None:
        self.query_one(TextLog).write("-" * 50)
        self.query_one(MessageSource).send_indirectly_after_refresh()

    @on(MessageSource.Boop)
    def report(self) -> None:
        self.query_one(TextLog).write("App got boop")


if __name__ == "__main__":
    DelayedMessageApp().run()
