"""Currently doesn't work!"""

from textual.app import App, ComposeResult
from textual.containers import Container
from textual.css.scalar import Scalar, Unit
from textual.widgets import Header, Footer


class AniApp(App[None]):

    BINDINGS = [("1", "height(1)", "1"), ("0", "height(100)", "100")]

    CSS = """
    Container {
        background: red;
    }
    """

    def compose(self) -> ComposeResult:
        yield Header()
        yield Container(id="box")
        yield Footer()

    def action_height(self, pcent: float) -> None:
        self.query_one("#box", Container).styles.animate(
            "height", value=Scalar(float(pcent), Unit.HEIGHT, Unit.HEIGHT), duration=2.0
        )


if __name__ == "__main__":
    AniApp().run()
