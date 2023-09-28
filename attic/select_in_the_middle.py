"""https://discord.com/channels/1026214085173461072/1033754296224841768/1142074926594007131"""

from textual.app import App, ComposeResult
from textual.containers import Vertical, Center
from textual.widgets import Select, Label, Input, Button

class SelectInTheMiddleApp(App[None]):

    CSS = """
    Select {
        width: 50%;
    }
    """
    def compose(self) -> ComposeResult:
        with Vertical():
            with Center():
                yield Select((("One", "One"), ("Two", "Two"), ("Three", "Three")))
            with Center():
                yield Label("Here is some text that goes in the middle")
            with Center():
                yield Input()
            with Center():
                yield Button("Don't press me I don't do owt")

if __name__ == "__main__":
    SelectInTheMiddleApp().run()
