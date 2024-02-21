from textual.app import App, ComposeResult
from textual.containers import Vertical
from textual.widgets import Header, Footer, Label


class LabelH1(Label): ...


class CSSOddnessApp(App[None]):

    CSS = """
    Vertical LabelH1 {
        background: red;
    }
    """

    def compose(self) -> ComposeResult:
        yield Header()
        yield Vertical(
            Label("Label"),
            LabelH1("LabelH1"),
        )
        yield Footer()


if __name__ == "__main__":
    CSSOddnessApp().run()
