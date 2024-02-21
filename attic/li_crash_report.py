"""https://github.com/Textualize/textual/issues/2912"""

from __future__ import annotations

from textual.widget import Widget
from textual.widgets import Label, LoadingIndicator
from textual.app import App, ComposeResult
from textual.containers import Vertical, Horizontal, Container
from textual.screen import Screen


class LoadingWidget(Widget):

    def compose(self) -> ComposeResult:
        with Vertical():
            yield LoadingIndicator()


class WorkerTest(Widget):

    def __init__(
        self,
    ) -> None:
        super().__init__()

    def compose(self) -> ComposeResult:
        with Horizontal():
            yield LoadingWidget()


class DummyWidget(Widget):
    def __init__(
        self,
    ):
        super().__init__()

    def compose(self) -> ComposeResult:
        with Container():
            yield Label("Test")
            yield WorkerTest()


class MainScreen(Screen):

    def compose(self) -> ComposeResult:
        with Vertical():
            with Horizontal():
                yield Container(LoadingWidget(), id="left")

    def on_mount(self) -> None:
        self.set_timer(2, self.update_widgets)

    async def update_widgets(
        self,
    ):
        await self.query_one("#left").remove()
        self.query_one(Horizontal).mount(DummyWidget())


class DemoApp(App[None]):

    def on_mount(self) -> None:
        self.push_screen(MainScreen())


if __name__ == "__main__":
    DemoApp().run()
