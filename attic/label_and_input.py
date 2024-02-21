from textual.app import App, ComposeResult
from textual.containers import Horizontal
from textual.widgets import Label, Input


class LabelAndInput(Horizontal):

    DEFAULT_CSS = """
    LabelAndInput {
        height: auto;
    }

    LabelAndInput Input {
        width: 1fr;
    }

    LabelAndInput Label {
        height: 3;
        content-align: right middle;
    }
    """

    def compose(self) -> ComposeResult:
        """Compose the child widgets."""
        yield Label("Label")
        yield Input()


class LabelAndInputWidgetApp(App[None]):

    def compose(self) -> ComposeResult:
        yield LabelAndInput()
        yield LabelAndInput()
        yield LabelAndInput()


if __name__ == "__main__":
    LabelAndInputWidgetApp().run()

### label_and_input.py ends here
