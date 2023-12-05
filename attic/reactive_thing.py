from textual.app import App, ComposeResult, RenderResult
from textual.reactive import reactive
from textual.widget import Widget

class ToggleMessage(Widget):

    state: reactive[bool] = reactive(False)

    def render(self) -> RenderResult:
        return "ON" if self.state else "OFF"

class ReactiveExampleApp(App[None]):

    def compose(self) -> ComposeResult:
        yield ToggleMessage()

    def toggle(self) -> None:
        self.query_one(ToggleMessage).state = not self.query_one(ToggleMessage).state

    def on_mount(self) -> None:
        self.set_interval(1, self.toggle)

if __name__ == "__main__":
    ReactiveExampleApp().run()
