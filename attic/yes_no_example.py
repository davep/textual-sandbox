from textual.app import App, ComposeResult
from textual.containers import Vertical, Horizontal
from textual.message import Message
from textual.screen import Screen, ModalScreen
from textual.widgets import Header, Footer, Button, Label
from textual.widget import Widget


class YesNo(ModalScreen):

    DEFAULT_CSS = """
    YesNoDialog {
        align: center middle;
    }

    YesNoDialog > Vertical {
        background: $panel;
        height: auto;
        width: auto;
        border: thick $primary;
    }
    """

    class YesResult(Message):
        pass

    class NoResult(Message):
        pass

    def __init__(self, asker: Widget) -> None:
        super().__init__()
        self._asker = asker

    def compose(self) -> ComposeResult:
        """Compose the child widgets."""
        with Vertical():
            yield Label("Well, what say you? Aye or naw?")
            with Horizontal():
                yield Button("Aye", id="aye")
                yield Button("Naw", id="naw")

    def on_button_pressed(self, event: Button.Pressed) -> None:
        self._asker.post_message(
            (self.YesResult if event.button.id == "aye" else self.NoResult)()
        )
        self.app.pop_screen()


class Main(Screen):

    DEFAULT_CSS = """
    Main {
        align: center middle;
    }
    """

    BINDINGS = [
        ("space", "ask", "Ask the question"),
    ]

    def compose(self) -> ComposeResult:
        yield Header()
        yield Label()
        yield Footer()

    def action_ask(self) -> None:
        self.app.push_screen(YesNo(self))

    def on_yes_no_yes_result(self, event: YesNo.YesResult) -> None:
        self.query_one(Label).update("Computer says yes")

    def on_yes_no_no_result(self, event: YesNo.NoResult) -> None:
        self.query_one(Label).update("Computer says no")


class YesNoExampleApp(App[None]):

    def on_mount(self) -> None:
        self.push_screen(Main())


if __name__ == "__main__":
    YesNoExampleApp().run()
