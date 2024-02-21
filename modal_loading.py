"""Example of using a loading indicator as a loading modal."""

from textual.app import App, ComposeResult
from textual.screen import ModalScreen
from textual.widgets import LoadingIndicator


class LoadingScreen(ModalScreen[None]):

    CSS = """
    LoadingScreen {
        align: center middle;
        LoadingIndicator {
            width: 50%;
            height: 3;
        }
    }
    """

    def compose(self) -> ComposeResult:
        yield LoadingIndicator()


class LoadingIndicatorModalScreenApp(App[None]):

    CSS = """
    Screen#_default {
        background: red;
    }
    """

    def on_mount(self) -> None:
        self.push_screen(LoadingScreen())


if __name__ == "__main__":
    LoadingIndicatorModalScreenApp().run()

### modal_loading.py ends here
