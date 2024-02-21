"""https://discord.com/channels/1026214085173461072/1033754296224841768/1143635923045728277"""

from textual.app import App, ComposeResult
from textual.screen import Screen
from textual.widgets import Input


class InputScreen(Screen):

    def compose(self) -> ComposeResult:
        yield Input()


class UpperScreen(Screen):

    def on_mount(self) -> None:
        self.app.push_screen(InputScreen())

    def on_input_changed(self) -> None:
        self.app.bell()


class DoesInputChangedBubbleTooFarApp(App[None]):

    def on_mount(self) -> None:
        self.push_screen(UpperScreen())


if __name__ == "__main__":
    DoesInputChangedBubbleTooFarApp().run()

### does_input_bubble_too_far.py ends here
