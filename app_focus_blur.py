"""Test application focus."""

from pathlib import Path

from textual.app import App, ComposeResult
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


if __name__ == "__main__":
    AppFocusBlurApp().run()

### app_focus_blur.py ends here
