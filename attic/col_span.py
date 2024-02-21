from textual.app import App, ComposeResult
from textual.widgets import Label


class ColSpanApp(App[None]):

    CSS = """
    Screen {
        layout: grid;
        grid-size: 2;
    }

    Label {
        width: 1fr;
        border: solid green;
    }

    #label2 {
        column-span: 2;
    }
    """

    def compose(self) -> ComposeResult:
        yield Label("Label 1", id="label1")
        yield Label("Label 2", id="label2")


if __name__ == "__main__":
    ColSpanApp().run()

### col_span.py ends here
