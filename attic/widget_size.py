"""https://github.com/Textualize/textual/discussions/3527"""

from textual.app import App, ComposeResult
from textual.widgets import Static

class WidgetSizeApp(App[None]):

    CSS = """
    #fr1 {
        height: 1fr;
    }
    #fr2 {
        height: 2fr;
    }
    """

    def compose(self) -> ComposeResult:
        yield Static(id="fr1")
        yield Static(id="fr2")

    def on_mount(self) -> None:
        self.call_after_refresh(self.show_sizes)

    def on_resize(self) -> None:
        self.call_after_refresh(self.show_sizes)

    def show_sizes(self) -> None:
        for widget in self.query(Static):
            widget.update(f"{widget.size!r}")

if __name__ == "__main__":
    WidgetSizeApp().run()

### widget_size.py ends here
