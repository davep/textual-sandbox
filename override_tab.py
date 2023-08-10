"""https://discord.com/channels/1026214085173461072/1033754296224841768/1139139459644915804"""

from textual.app import App, ComposeResult
from textual.binding import Binding
from textual.widgets import Button

class OverrideTabApp(App[None]):

    BINDINGS = [
        Binding("tab", "nope", priority=True),
    ]

    def compose(self) -> ComposeResult:
        for _ in range(10):
            yield Button("Nope")

    def action_nope(self) -> None:
        self.notify("Nope")

if __name__ == "__main__":
    OverrideTabApp().run()
