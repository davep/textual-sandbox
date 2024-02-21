from textual import on
from textual.app import App, ComposeResult
from textual.reactive import reactive
from textual.message import Message
from textual.widget import Widget
from textual.widgets import Log


class TestWidget(Widget):

    value: reactive[str] = reactive("Hello, World!")

    class Computed(Message):
        pass

    def compute_value(self) -> str:
        self.post_message(self.Computed())
        return "Wat?"


class ComputeTestApp(App[None]):

    CSS = """
    TestWidget, Log {
        border: solid red;
        height: 1fr;
    }
    """

    def compose(self) -> ComposeResult:
        yield TestWidget()
        yield Log()

    @on(TestWidget.Computed)
    def log_message(self, event: TestWidget.Computed) -> None:
        self.query_one(Log).write_line(f"{event!r}")


if __name__ == "__main__":
    ComputeTestApp().run()

### compute_test.py ends here
