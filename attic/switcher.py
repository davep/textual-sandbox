"""https://github.com/Textualize/textual/discussions/3747"""

from textual.app import App, ComposeResult
from textual.screen import Screen
from textual.widgets import Label

class Info(Screen):

    BINDINGS = [
        ("space", "switch_screen('home')"),
    ]

    def compose(self) -> ComposeResult:
        self.app.bell()
        yield Label("This is the info screen.")

    def on_screen_resume(self) -> None:
        self.notify("Hey look I'm back!")


class Home(Screen):

    BINDINGS = [
        ("space", "switch_screen('info')"),
    ]

    def compose(self) -> ComposeResult:
        self.app.bell()
        yield Label("This is the home screen.")

class SwitchScreenApp(App[None]):

    SCREENS = {
        "home": Home(),
        "info": Info(),
    }

    def on_mount(self) -> None:
        self.push_screen("home")

if __name__ == "__main__":
    SwitchScreenApp().run()

### switcher.py ends here
