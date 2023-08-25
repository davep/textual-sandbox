from textual import on
from textual.app import App, ComposeResult
from textual.containers import Horizontal, Vertical
from textual.screen import ModalScreen
from textual.widgets import Label, OptionList, Button
from textual.widgets.option_list import Option

class OptionsDialog(ModalScreen[str]):

    DEFAULT_CSS = """
    OptionsDialog {
        align: center middle;
    }

    OptionsDialog > Vertical {
        background: $panel;
        height: 60%;
        width: 60%;
        border: thick $primary;
    }

    OptionsDialog Label {
        width: 100%;
        content-align: center middle;
    }

    OptionsDialog #input {
        height: 1fr;
    }

    OptionsDialog OptionList {
        height: 1fr;
    }

    OptionsDialog #buttons {
        width: 100%;
        height: auto;
        align-horizontal: right;
        padding-right: 1;
    }
    """

    def compose(self) -> ComposeResult:
        """Compose the child widgets."""
        with Vertical():
            with Vertical(id="input"):
                yield Label("Select a thing from the list of things")
                yield OptionList(*[
                    Option(f"This is option thing {n}", id=str(n)) for n in range(100)
                ])
            with Horizontal(id="buttons"):
                yield Button("OK", id="ok", variant="primary")
                yield Button("Cancel", id="cancel")

    @on(Button.Pressed, "#ok")
    @on(OptionList.OptionSelected)
    def return_chosen(self):
        self.query_one
        option_list = self.query_one(OptionList)
        self.dismiss(option_list.get_option_at_index(option_list.highlighted).id)

    @on(Button.Pressed, "#cancel")
    def user_canceled(self) -> None:
        self.app.pop_screen()

class OptionListDialogApp(App[None]):

    def compose(self) -> ComposeResult:
        yield Label("The chosen option will go here")
        yield Button("Press me to test the dialog")

    def show_result(self, result: str) -> None:
        self.query_one(Label).update(result)

    @on(Button.Pressed)
    def ask(self) -> None:
        self.push_screen(OptionsDialog(), callback=self.show_result)

if __name__ == "__main__":
    OptionListDialogApp().run()
