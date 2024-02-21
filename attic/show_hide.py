from textual.app import App, ComposeResult
from textual.containers import Container
from textual.widgets import Static, Input, Button
from textual.reactive import reactive


class SwapContent(Container):

    DEFAULT_CSS = """
    SwapContent {
        height: auto;
        border: solid red;
        background: #444;
        height: 5;
    }

    .hidden {
        display: none;
    }
    """

    allow_edit = reactive(False)

    def compose(self) -> ComposeResult:
        yield Static("This is just some static text", id="text")
        yield Input(placeholder="This is an input field", id="input", classes="hidden")

    def watch_allow_edit(self, allow_edit: bool) -> None:
        self.query_one("#text", Static).set_class(allow_edit, "hidden")
        self.query_one("#input", Input).set_class(not allow_edit, "hidden")


class SwapApp(App[None]):

    def compose(self) -> ComposeResult:
        yield SwapContent()
        yield Button("Toggle edit", id="toggle")

    def on_button_pressed(self, event: Button.Pressed) -> None:
        if event.button.id == "toggle":
            swapper = self.query_one(SwapContent)
            swapper.allow_edit = not swapper.allow_edit


if __name__ == "__main__":
    SwapApp().run()
