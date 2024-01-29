from textual.app import App, ComposeResult
from textual.widget import Widget
from textual.widgets import Static

class NotACounter(Widget):
    ALLOW_CHILDREN = False

class NoChildren4(App[None]):

    def compose(self) -> ComposeResult:
        yield NotACounter(Static("Hello"))

if __name__ == "__main__":
    NoChildren4().run()
