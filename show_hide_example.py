"""https://github.com/Textualize/textual/discussions/3394"""

from textual import on
from textual.app import App, ComposeResult
from textual.containers import Vertical
from textual.widgets import Select, Static, Input

class ShowHideExampleApp(App[None]):

    CSS = """
    Vertical > Static {
        height: 1fr;
        background: red;
    }

    .hidden {
        display: none;
    }
    """

    def compose(self) -> ComposeResult:
        with Vertical():
            yield Select(
                (("Show", "show"), ("Hide", "hide")),
                value="hide", allow_blank=False
            )
            yield Static("Show/hide me", classes="hidden")
            yield Input(placeholder="This comes after")

    @on(Select.Changed)
    def show_hide(self, event: Select.Changed) -> None:
        self.query_one("Vertical > Static").set_class(
            event.value == "hide", "hidden"
        )

if __name__ == "__main__":
    ShowHideExampleApp().run()

### show_hide_example.py ends here
