"""https://github.com/Textualize/textual/issues/1355"""

from textual.app import App, ComposeResult
from textual.widgets import Header, Footer, Label, Button
from textual.containers import Vertical


class ShowHideApp(App[None]):

    CSS = """
    Horizontal {
        height: 1fr;
        border: solid red;
    }
    Button {
       width: 100%;
       height: 3;
    }
    Label {
        width: 100%;
        height: 9fr;
        content-align: center middle;
        background: #888800;
        visibility: visible;
    }

    .hidden {
        visibility: hidden;
    }
    """

    def compose(self) -> ComposeResult:
        yield Header()
        yield Vertical(
            Vertical(
                Button("Toggle show/hide via code", id="via-code"),
                Label(
                    "I can be toggled via code; press the button", id="via-code-label"
                ),
            ),
            Vertical(
                Button("Toggle show/hide via classes", id="via-classes"),
                Label(
                    "I can be toggled via classes; press the button",
                    id="via-classes-label",
                ),
            ),
        )
        yield Footer()

    def on_button_pressed(self, event: Button.Pressed) -> None:
        if event.button.id == "via-code":
            label = self.query_one("#via-code-label")
            label.styles.visibility = (
                "visible" if label.styles.visibility == "hidden" else "hidden"
            )
        elif event.button.id == "via-classes":
            self.query_one("#via-classes-label").toggle_class("hidden")


if __name__ == "__main__":
    ShowHideApp().run()
