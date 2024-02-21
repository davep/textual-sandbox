from textual.app import App, ComposeResult
from textual.widgets import Static


class StaticSize(App[None]):

    def compose(self) -> ComposeResult:
        yield Static()

    def on_mount(self) -> None:
        s = self.query_one(Static)
        self.query_one(Static).update(
            f"Width: {s.styles.width}, Height: {s.styles.height}"
        )


if __name__ == "__main__":
    StaticSize().run()
