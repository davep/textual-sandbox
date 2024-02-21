from textual.app import App, ComposeResult
from textual.widgets import Static


class NoChildren1(App[None]):

    def compose(self) -> ComposeResult:
        yield Static()

    def on_mount(self) -> None:
        self.query_one(Static).mount(Static("Hello"))


if __name__ == "__main__":
    NoChildren1().run()
