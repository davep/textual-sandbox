from textual.app import App, ComposeResult
from textual.widgets import Label, Input, Button


class MyOwnSuperCoolFocusThing(Label, can_focus=True):

    DEFAULT_CSS = """
    MyOwnSuperCoolFocusThing {
        border: solid darkred;
    }

    MyOwnSuperCoolFocusThing:focus {
        border: solid red;
    }
    """


class FocusDemo(App[None]):

    CSS = """
    Screen {
        align: center middle;
    }
    """

    def compose(self) -> ComposeResult:
        yield Label("This is a label, it can't get focus")
        yield Input(placeholder="This is an input, it can get focus")
        yield Button("This is a button, it can get focus")
        yield MyOwnSuperCoolFocusThing(
            "While this is a label, I've made it so it can focus"
        )

    def on_mount(self) -> None:
        # When the app starts, we force focus to the input and then focus
        # won't be lost again.
        self.query_one(Input).focus()


if __name__ == "__main__":
    FocusDemo().run()
