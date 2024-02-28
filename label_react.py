"""To answer https://stackoverflow.com/questions/78009587/python-textual-widget-not-refreshing

But answered on Discord, where it was asked.
"""

from textual.app import App, ComposeResult
from textual.reactive import reactive
from textual.widgets import Footer, Header, Input, Label, Static


class TestBody(Static):
    data = reactive("")

    def compose(self) -> ComposeResult:
        yield Input()
        yield Label()

    def watch_data(self):
        self.query_one(Label).update(f"Data: {self.data}")

    def on_input_submitted(self, message):
        self.data = message.value


class MyApp(App):
    def compose(self) -> ComposeResult:
        yield Header()
        yield TestBody()
        yield Footer()


if __name__ == "__main__":
    MyApp().run()

### label_react.py ends here
