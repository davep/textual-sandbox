from textual.app import App, ComposeResult
from textual.containers import Grid, Vertical
from textual.widgets import Header, Footer, Button, TextLog


class FocusLogButton(Button):

    def log_focus(self, handler: str) -> None:
        self.screen.query_one(TextLog).write(
            f"{handler} - {self.id=} - {self.has_focus=}"
        )

    def on_focus(self) -> None:
        self.log_focus("on_focus")

    def on_blur(self) -> None:
        self.log_focus("on_blur")


class KnowingFocusApp(App[None]):

    CSS = """
    Grid {
        grid-size: 5;
        align: center middle;
    }
    """

    def compose(self) -> ComposeResult:
        yield Header()
        with Vertical():
            with Grid():
                for n in range(25):
                    yield FocusLogButton(str(n), id=f"button-{n}")
            yield TextLog()
        yield Footer()


if __name__ == "__main__":
    KnowingFocusApp().run()
