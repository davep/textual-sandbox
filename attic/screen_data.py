"""https://github.com/Textualize/textual/discussions/3496"""

from textual import on
from textual.app import App, ComposeResult
from textual.screen import Screen
from textual.widgets import Button


class Child(Screen[bool]):

    def compose(self) -> ComposeResult:
        yield Button("Enable", id="enable")
        yield Button("Disable", id="disable")

    @on(Button.Pressed)
    def decide(self, event: Button.Pressed) -> None:
        self.dismiss(event.control.id == "enable")


class Main(Screen):

    def compose(self) -> ComposeResult:
        yield Button("This will enable/disable", id="tester")
        yield Button("Show child screen", id="show-child")

    def enable_disable(self, enable: bool) -> None:
        self.query_one("#tester").disabled = not enable

    @on(Button.Pressed, "#show-child")
    def show_child(self) -> None:
        self.app.push_screen(Child(), callback=self.enable_disable)


class PassingScreenDataApp(App[None]):

    def on_mount(self) -> None:
        self.push_screen(Main())


if __name__ == "__main__":
    PassingScreenDataApp().run()

### screen_data.py ends here
