from textual import on
from textual.app import App, ComposeResult
from textual.widgets import TextArea

class MultiLineApp(App[None]):

    CSS = """
    TextArea {
        height: 1;
    }

    TextArea.lotsalines {
        height: 1fr;
    }
    """

    def compose(self) -> ComposeResult:
        yield TextArea()

    @on(TextArea.Changed)
    def input_size(self, event: TextArea.Changed) -> None:
        event.control.set_class(event.control.document.line_count > 1, "lotsalines")

if __name__ == "__main__":
    MultiLineApp().run()

### multiline_text.py ends here
