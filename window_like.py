"""Example of a window-like effect."""

from textual.app import App, ComposeResult
from textual.events import Click
from textual.geometry import Offset
from textual.widget import Widget
from textual.widgets import Placeholder


class Window(Placeholder):
    DEFAULT_CSS = """
    Window {
        overlay: screen;
    }
    """

    def __init__(self, x: int, y: int, width: int, height: int) -> None:
        super().__init__()
        self.offset = Offset(x, y)
        self.styles.width = width
        self.styles.height = height

    async def _on_click(self, _: Click) -> None:
        if isinstance(self.parent, Widget):
            self.parent.move_child(self, after=-1)
        return await super()._on_click(_)


class WindowLikeApp(App[None]):
    def compose(self) -> ComposeResult:
        yield Window(3, 3, 20, 10)
        yield Window(4, 7, 22, 12)
        yield Window(7, 10, 20, 10)


if __name__ == "__main__":
    WindowLikeApp().run()

### window_like.py ends here
