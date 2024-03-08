"""Test application focus."""

from pathlib import Path

from textual import on
from textual.app import App, ComposeResult
from textual.events import AppBlur, AppFocus
from textual.widgets import Digits, Input, TextArea


class AppFocusBlurApp(App[None]):
    def compose(self) -> ComposeResult:
        yield Digits("")
        yield Input(placeholder="Here's an input to help test")
        yield TextArea(Path(__file__).read_text(), language="python")

    def update_digits(self) -> None:
        self.query_one(Digits).update(
            ("1" if self.app_focus else "0") * (self.size.width // 3)
        )

    def on_mount(self) -> None:
        self.update_digits()

    def watch_app_focus(self) -> None:
        self.update_digits()

    def sneak_focus_back(self) -> None:
        self.query_one(Input).focus()

    @on(AppBlur)
    def goodbye(self) -> None:
        self.notify("Wait! Don't go! Come back!")
        self.set_timer(0.5, self.sneak_focus_back)

    @on(AppFocus)
    def hello(self) -> None:
        self.notify("Pfft! Need me again do you? :-P")


if __name__ == "__main__":
    AppFocusBlurApp().run()

### app_focus_blur.py ends here
