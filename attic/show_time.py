from datetime import datetime
from textual.app import App, ComposeResult, RenderableType
from textual.widgets import Label


class Time(Label):

    def on_mount(self) -> None:
        self.auto_refresh = 0.1

    def render(self) -> RenderableType:
        return str(datetime.now())


class TimeApp(App[None]):

    def compose(self) -> ComposeResult:
        yield Time()


if __name__ == "__main__":
    TimeApp().run()
