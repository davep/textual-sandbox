from textual.app import App, ComposeResult
from textual.widgets import Static


class DodgyStatic(Static):

    def compose(self) -> ComposeResult:
        yield Static("Hello")


class NoChildren2(App[None]):

    def compose(self) -> ComposeResult:
        yield DodgyStatic()


if __name__ == "__main__":
    NoChildren2().run()
