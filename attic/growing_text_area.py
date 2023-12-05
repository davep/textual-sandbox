from textual.app import App, ComposeResult
from textual.widgets import TextArea

class GrowingTextAreaApp(App[None]):

    CSS = """
    TextArea {
        height: auto;
        max-height: 100%;
        border: solid red;
    }
    """

    def compose(self) -> ComposeResult:
        yield TextArea()

if __name__ == "__main__":
    GrowingTextAreaApp().run()

### growing_text_area.py ends here
