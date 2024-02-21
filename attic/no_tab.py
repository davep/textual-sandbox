from textual.app import App, ComposeResult
from textual.widgets import Input, Button
from textual.events import Key


class NoTab(App[None]):

    def compose(self) -> ComposeResult:
        for n in range(5):
            yield Input()
        for n in range(5):
            yield Button(str(n))

    def on_mount(self):
        self.query(Input).first().focus()

    def on_key(self, event: Key):
        if event.key == "tab":
            event.prevent_default()


if __name__ == "__main__":
    NoTab().run()
