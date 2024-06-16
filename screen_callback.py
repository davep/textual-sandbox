"""Evidence that screen callbacks are still working.

For a reply to https://github.com/Textualize/textual/issues/4656.
"""

from textual import on
from textual.app import App, ComposeResult
from textual.screen import Screen
from textual.widgets import Button


class Test(Screen[str]):
    def compose(self) -> ComposeResult:
        yield Button("Yes", id="Yes")
        yield Button("No", id="No")

    @on(Button.Pressed)
    def test_the_callback(self, event: Button.Pressed) -> None:
        assert event.button.id is not None
        self.dismiss(event.button.id)


class ScreenCallbackTest(App[None]):
    def compose(self) -> ComposeResult:
        yield Button("Test")

    @on(Button.Pressed)
    def test_screen_callback(self) -> None:
        def show_result(result: str) -> None:
            self.notify(result)

        self.push_screen(Test(), callback=show_result)


if __name__ == "__main__":
    ScreenCallbackTest().run()

### screen_callback.py ends here
