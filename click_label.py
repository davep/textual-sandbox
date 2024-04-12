"""Examples of clickable labels."""

from __future__ import annotations

from dataclasses import dataclass

from textual import on
from textual.app import App, ComposeResult
from textual.message import Message
from textual.widgets import Label


class ClickableLabel(Label):
    @dataclass
    class Click(Message):
        label: ClickableLabel

        @property
        def control(self) -> ClickableLabel:
            return self.label

    def on_click(self) -> None:
        self.post_message(self.Click(self))


class ClickLabelApp(App[None]):
    def compose(self) -> ComposeResult:
        yield ClickableLabel("You could inherit and add click support")
        yield Label("[@click=say_click]Or you could just use actions[/]")

    @on(ClickableLabel.Click)
    def say_clickable_label(self) -> None:
        self.notify("That was a clickable label")

    def action_say_click(self) -> None:
        self.notify("That was with a click action")


if __name__ == "__main__":
    ClickLabelApp().run()

### click_label.py ends here
