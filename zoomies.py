"""A window-a-like experience with max and restore."""

from textual.app import App, ComposeResult
from textual.events import Click
from textual.geometry import Offset
from textual.reactive import var
from textual.widget import Widget
from textual.widgets import Placeholder


class Window(Placeholder, can_focus=True):
    DEFAULT_CSS = """
    Window {
        overlay: screen;
        border: blank;

        &:focus {
            border: double;
        }
    }
    """

    is_zoomed: var[bool] = var(False)

    def __init__(self, x: int, y: int, width: int, height: int) -> None:
        super().__init__()
        self._restored_offset = Offset(x, y)
        self._restored_width = width
        self._restored_height = height

    async def _on_click(self, _: Click) -> None:
        if isinstance(self.parent, Widget):
            self.parent.move_child(self, after=-1)
        return await super()._on_click(_)

    def give_zoomies(self) -> None:
        self.offset = Offset(0, 0)
        self.styles.width = "100vw"
        self.styles.height = "100vh"

    def no_more_zoomies(self) -> None:
        self.offset = self._restored_offset
        self.styles.width = self._restored_width
        self.styles.height = self._restored_height

    def _watch_is_zoomed(self) -> None:
        if self.is_zoomed:
            self.give_zoomies()
        else:
            self.no_more_zoomies()

    def key_space(self) -> None:
        self.is_zoomed = not self.is_zoomed


class WindowLikeWithZoomiesApp(App[None]):
    def compose(self) -> ComposeResult:
        yield Window(3, 3, 40, 20)
        yield Window(22, 7, 44, 22)
        yield Window(12, 15, 40, 20)


if __name__ == "__main__":
    WindowLikeWithZoomiesApp().run()

### zoomies.py ends here
