from textual.app import App, ComposeResult
from textual.containers import VerticalScroll
from textual.events import Key
from textual.screen import Screen
from textual.widgets import Static

class TheScreen(Screen):

    def on_key(self, event: Key):
        exclude_events = ["up", "down", "left", "right", "pageup", "pagedown", "home", "end"]
        if event.key not in exclude_events:
            self.app.pop_screen()

    def compose(self) -> ComposeResult:
        yield VerticalScroll(Static(
            "\n".join(
                f"This is line number {n}" for n in range(1000)
            )
        ))

class VerticalScrollAndOnKeyApp(App[None]):

    def on_mount(self) -> None:
        self.push_screen(TheScreen())

if __name__ == "__main__":
    VerticalScrollAndOnKeyApp().run()
