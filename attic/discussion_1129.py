from textual.app import App, ComposeResult
from textual.widgets import Static, Button
from textual.containers import Horizontal


class Discussion1129(App[str]):

    CSS = """
    #question {
        border: solid green;
    }

    Button {
        margin: 2;
    }
    """

    BINDINGS = [("y", "result( 'y' )", ""), ("n", "result( 'n' )", "")]

    def compose(self) -> ComposeResult:
        yield Static(
            "A strange game. The only winning move is not to play. How about a nice game of chess?",
            id="question",
        )
        yield Horizontal(Button("Yes please", id="y"), Button("No thanks", id="n"))

    def on_button_pressed(self, event: Button.Pressed) -> None:
        self.action_result(event.button.id)

    def action_result(self, answer: str):
        self.exit(answer)


if __name__ == "__main__":
    print(Discussion1129().run())
