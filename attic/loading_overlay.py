"""https://github.com/Textualize/textual/issues/3677"""

from textual.app import App, ComposeResult
from textual.widgets import Label


class LoadingOverlayApp(App[None]):

    CSS = """
    Label {
        width: 90%;
        height: 1fr;
        text-align: center;
        border: solid red;
    }
    """

    def compose(self) -> ComposeResult:
        yield Label("This is a really big label")

    def on_mount(self) -> None:
        self.notify(
            "This is a really big notification. Loading should not overwrite it.",
            timeout=9_999_999,
        )
        self.query_one(Label).loading = True


if __name__ == "__main__":
    LoadingOverlayApp().run()

### loading_overlay.py ends here
