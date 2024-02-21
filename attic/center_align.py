from textual.app import App, ComposeResult
from textual.containers import Vertical, Horizontal
from textual.widgets import Header, Footer, Button, Label, Input


class CenterApp(App[None]):

    CSS = """
    Vertical {
        border: round red;
        align: center middle;
    }

    Horizontal {
        width: 100%;
        height: auto;
        align: center middle;
    }

    Label {
        border: round yellow;
    }

    Input {
        width: 50%;
    }
    """

    def compose(self) -> ComposeResult:
        yield Header()
        yield Vertical(
            Horizontal(Label("This is a label")),
            Horizontal(Button("This is a button, it's longer")),
            Horizontal(Input(placeholder="This is an input, it's even longer still")),
        )
        yield Footer()


if __name__ == "__main__":
    CenterApp().run()
