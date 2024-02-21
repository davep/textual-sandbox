from textual.app import App, ComposeResult
from textual.containers import Vertical
from textual.widgets import Header, Footer, Label, Input


class InputPlaybround(App[None]):

    CSS = """
    Label {
        margin-left: 1;
    }
    """

    def compose(self) -> ComposeResult:
        yield Header()
        yield Vertical(
            Label("Empty Input:"),
            Input(placeholder="This input has nothing in it"),
            Label("One Letter Input:"),
            Input("A"),
            Label("Many Letters Input:"),
            Input("A" * 50),
            Label("Two Words Input:"),
            Input("Hello There"),
            Label("Many Words Input:"),
            Input("At last we will reveal ourselves to the Jedi"),
            Label("Punctuated Text:"),
            Input(
                "At last we will reveal ourselves to the Jedi. At last we will have revenge."
            ),
            Label("Hyphenated Text:"),
            Input("This is some test-text to see what will happen"),
        )
        yield Footer()


if __name__ == "__main__":
    InputPlaybround().run()
