"""Example of transition with offset."""

from textual.app import App, ComposeResult
from textual.widgets import Static


class AnimateOffsetApp(App[None]):
    CSS = """
    Static {
        border: solid red;
        offset-x: -100%;
        transition: offset 1000ms in_out_cubic;

        &.slide-in {
            offset-x: 50%;
        }
    }
    """

    BINDINGS = [
        ("space", "animate"),
    ]

    def compose(self) -> ComposeResult:
        yield Static("Press space to animate me!")

    def action_animate(self) -> None:
        self.query_one(Static).toggle_class("slide-in")


if __name__ == "__main__":
    AnimateOffsetApp().run()

### transition_offset.py ends here
