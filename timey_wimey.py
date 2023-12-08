from time import sleep

from textual import on, work
from textual.app import App, ComposeResult
from textual.message import Message
from textual.widgets import Button

class TimeyWimeyApp(App[None]):

    CSS = """
    Screen {
        align: center middle;
    }
    """

    def compose(self) -> ComposeResult:
        yield Button("Do some work!")

    @on(Button.Pressed)
    def travel_in_time(self) -> None:
        self.screen.loading = True
        self.tardis()

    class Vwoorp(Message):
        pass

    @on(Vwoorp)
    def arrive(self) -> None:
        self.screen.loading = False

    @work(thread=True)
    def tardis(self) -> None:
        sleep(5)
        self.post_message(self.Vwoorp())

if __name__ == "__main__":
    TimeyWimeyApp().run()

### timey_wimey.py ends here
