from textual.app import App, ComposeResult
from textual.containers import Horizontal, Vertical
from textual.screen import ModalScreen
from textual.widgets import Header, Footer, OptionList, Button, Label


class AyeNaw(ModalScreen[bool]):
    DEFAULT_CSS = """
    AyeNaw {
        align: center middle;
    }

    AyeNaw > Vertical {
        background: $secondary;
        width: auto;
        height: auto;
        border: thick $primary;
        padding: 2 4;
    }

    AyeNaw > Vertical > * {
        width: auto;
        height: auto;
    }

    AyeNaw > Vertical > Label {
        padding-bottom: 2;
    }

    AyeNaw > Vertical > Horizontal {
        align: right middle;
    }

    AyeNaw Button {
        margin-left: 2;
    }
    """

    def compose(self) -> ComposeResult:
        with Vertical():
            yield Label("Well, what do you think?")
            with Horizontal():
                yield Button("Aye!", id="aye")
                yield Button("Naw!", id="naw")

    def on_button_pressed(self, event: Button.Pressed) -> None:
        self.dismiss(result=event.button.id == "aye")


class ScreenResultExampleApp(App[None]):
    BINDINGS = [
        ("question_mark", "ask", "Ask a question"),
    ]

    def compose(self) -> ComposeResult:
        yield Header()
        yield OptionList()
        yield Footer()

    def accept_answer(self, answer: bool) -> None:
        self.query_one(OptionList).add_option(
            f"Computer said {'[green]Aye' if answer else '[red]Naw'}[/]"
        )

    def action_ask(self) -> None:
        self.push_screen(AyeNaw(), callback=self.accept_answer)


if __name__ == "__main__":
    ScreenResultExampleApp().run()
