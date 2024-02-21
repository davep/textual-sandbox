from textual.app import App, ComposeResult
from textual.widgets import Label


class LabelOffsetExample(App[None]):

    CSS = """
    Label {
        transition: offset 500ms linear;
    }

    Label.other-spot {
        offset: 20 20;
    }
    """

    BINDINGS = [
        ("space", "toggle_class('Label', 'other-spot')"),
    ]

    def compose(self) -> ComposeResult:
        yield Label("Here is a label!")


if __name__ == "__main__":
    LabelOffsetExample().run()
