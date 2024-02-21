"""Example of loading stuff on startup, in a sub-screen."""

from time import sleep

from textual import work
from textual.app import App, ComposeResult
from textual.screen import Screen
from textual.widgets import Label


class LoadSomeStuff(Screen[str]):

    def compose(self) -> ComposeResult:
        yield Label("Just wait a wee while, we'll be done soon.")

    @work(thread=True)
    def load_stuff(self) -> None:
        sleep(5)
        self.app.call_from_thread(self.dismiss, "We got the data!")

    def on_mount(self) -> None:
        self.load_stuff()


class LoadingScreenApp(App[None]):

    def compose(self) -> ComposeResult:
        yield Label("The result will go in here.")

    def stuff_loaded(self, stuff: str) -> None:
        self.query_one(Label).update(stuff)

    def on_mount(self) -> None:
        self.push_screen(LoadSomeStuff(), callback=self.stuff_loaded)


if __name__ == "__main__":
    LoadingScreenApp().run()

### loading_screen.py ends here
