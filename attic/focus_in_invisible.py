from textual.app import App, ComposeResult
from textual.containers import Horizontal, Vertical
from textual.widgets import Button, Label


class InvisibleContainerFocusApp(App[None]):

    CSS = """
    #invisible {
        visibility: hidden;
    }

    #invisible > * {
        visibility: visible;
    }
    """

    def compose(self) -> ComposeResult:
        with Horizontal():
            with Vertical():
                yield Label("The container for this is visible")
                for _ in range(10):
                    yield Button()
            with Vertical(id="invisible"):
                yield Label("The container for this is invisible")
                for _ in range(10):
                    yield Button()


if __name__ == "__main__":
    InvisibleContainerFocusApp().run()
