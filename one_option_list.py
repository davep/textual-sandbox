from textual import on
from textual.app import App, ComposeResult
from textual.containers import Vertical
from textual.widgets import OptionList, TextLog
from textual.widgets.option_list import Option

class OptionListApp(App[None]):

    CSS = """
    OptionList {
        height: 4fr;
    }

    TextLog {
        height: 1fr;
    }
    """

    def compose(self) -> ComposeResult:
        with Vertical():
            yield OptionList()
            yield TextLog()

    def on_mount(self):
        for n in range(20):
            self.query_one(OptionList).add_option(Option(f"Here is option {n}"))
        self.log_highlighted()

    @on(OptionList.OptionHighlighted)
    def log_highlighted(self) -> None:
        highlighted = self.query_one(OptionList).highlighted
        self.query_one(TextLog).write(f"Highlighted: {highlighted!r}")

if __name__ == "__main__":
    OptionListApp().run()
