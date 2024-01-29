"""https://github.com/Textualize/textual/issues/3690"""

from textual.app import App, ComposeResult
from textual.containers import Vertical
from textual.screen import Screen
from textual.widgets import Label

class ClickLabel(Label):

    def action_click(self) -> None:
        self.notify("ClickLabel.action_click reporting in!")

class Clicker(Vertical):

    def compose(self) -> ComposeResult:
        yield Label("1: [@click=app.click]Click on this for an app action to fire[/]")
        yield Label("2: [@click=screen.click]Click on this for a screen action to fire[/]")
        yield Label("3: [@click=click]Click on this for this container's action to fire[/]")
        yield ClickLabel("4: [@click=click]Click on this for the custom widget's action to fire[/]")

    def action_click(self) -> None:
        self.notify("Clicker.action_click reporting in!")


class MainScreen(Screen):

    def compose(self) -> ComposeResult:
        yield Clicker()

    def action_click(self) -> None:
        self.notify("Screen.action_click reporting in!")


class ClickBaitApp(App[None]):

    def on_mount(self) -> None:
        self.push_screen(MainScreen())

    def action_click(self) -> None:
        self.notify("App.action_click reporting in!")


if __name__ == "__main__":
    ClickBaitApp().run()

### click_bait.py ends here
