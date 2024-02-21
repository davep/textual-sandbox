from textual.app import App, ComposeResult
from textual.widgets import Label


class BoomApp(App[None]):

    def compose(self) -> ComposeResult:
        yield Label()

    def big_bada_boom(self) -> None:
        self.query_one(Label).update("BOOM!")

    def on_mount(self) -> None:
        self.set_timer(3, self.big_bada_boom)


if __name__ == "__main__":
    BoomApp().run()

### timer_example.py ends here
