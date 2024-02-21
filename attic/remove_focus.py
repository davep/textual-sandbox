from textual.app import App, ComposeResult
from textual.widgets import Input, Button


class RemoveFocusApp(App[None]):

    def compose(self) -> ComposeResult:
        for _ in range(5):
            yield Input()
            yield Button()

    def on_mount(self) -> None:
        self.call_after_refresh(self.screen.set_focus, None)


if __name__ == "__main__":
    RemoveFocusApp().run()
