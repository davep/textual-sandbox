"""Using a modal screen to get data.

For a question on Discord.
"""

from __future__ import annotations

from textual import on, work
from textual.app import App, ComposeResult
from textual.reactive import var
from textual.screen import ModalScreen
from textual.widgets import Button, Input, Label


class InputScreen(ModalScreen[str | None]):
    def compose(self) -> ComposeResult:
        yield Input()
        yield Button("Okay", id="ok")
        yield Button("Cancel", id="cancel")

    @on(Button.Pressed, "#ok")
    def okay(self) -> None:
        self.dismiss(self.query_one(Input).value)

    @on(Button.Pressed, "#cancel")
    def cancel(self) -> None:
        self.dismiss(None)


class DisplayInputExampleApp(App[None]):
    BINDINGS = [
        ("t", "get_data"),
    ]

    some_data: var[str] = var("")

    def compose(self) -> ComposeResult:
        yield Label()

    def watch_some_data(self) -> None:
        self.query_one(Label).update(f"The data: {self.some_data}")

    @work
    async def action_get_data(self) -> None:
        if (new_data := await self.push_screen_wait(InputScreen())) is not None:
            self.some_data = new_data


if __name__ == "__main__":
    DisplayInputExampleApp().run()

### text_from_modal.py ends here
