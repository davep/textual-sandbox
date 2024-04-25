"""Example to show that bindings work as expected with modals, etc."""

from textual import on, work
from textual.app import App, ComposeResult
from textual.binding import Binding
from textual.screen import ModalScreen, Screen
from textual.widgets import Button, Footer


class MyModal(ModalScreen[str]):
    BINDINGS = [
        Binding("f5", "gndn1", "Stuff"),
        Binding("f6", "gndn2", "Stuff"),
        Binding("f7", "gndn3", "Stuff"),
        Binding("f8", "gndn4", "Stuff"),
    ]

    def compose(self) -> ComposeResult:
        yield Button("Close me", id="close")
        yield Footer()

    @on(Button.Pressed, "#close")
    def back_we_go(self) -> None:
        self.dismiss("We're done!")


class Main(Screen[None]):
    BINDINGS = [
        Binding("f1", "gndn1", "Stuff"),
        Binding("f2", "gndn2", "Stuff"),
        Binding("f3", "gndn3", "Stuff"),
        Binding("f4", "gndn4", "Stuff"),
    ]

    def compose(self) -> ComposeResult:
        yield Button("Open the modal screen", id="open")
        yield Footer()

    @on(Button.Pressed, "#open")
    @work
    async def show_modal(self) -> None:
        self.notify(await self.app.push_screen_wait(MyModal()))


class ModalsAndBindingsApp(App[None]):
    def on_mount(self) -> None:
        self.push_screen(Main())


if __name__ == "__main__":
    ModalsAndBindingsApp().run()

### modals_and_bindings.py ends here
