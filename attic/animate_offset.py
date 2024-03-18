"""Example of animation with offset."""

from textual.app import App, ComposeResult
from textual.css.scalar import ScalarOffset
from textual.widgets import Static


class AnimateOffsetApp(App[None]):
    CSS = """
    Static {
        border: solid red;
        offset-x: -100%;
    }
    """

    BINDINGS = [
        ("space", "animate"),
    ]

    def compose(self) -> ComposeResult:
        yield Static("Press space to animate me!")

    def action_animate(self) -> None:
        self.query_one(Static).styles.animate(
            "offset", ScalarOffset.from_offset((0, 0)), duration=2
        )


if __name__ == "__main__":
    AnimateOffsetApp().run()

### animate_offset.py ends here
