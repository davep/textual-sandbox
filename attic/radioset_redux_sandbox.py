from textual.app import App, ComposeResult
from textual.containers import Vertical, Horizontal
from textual.widgets import Header, Footer, RadioSet, Input


class RadioSetReduxApp(App[None]):

    CSS = """
    Vertical {
        border: double green;
    }
    RadioSet {
        width: 1fr;
    }
    """

    def compose(self) -> ComposeResult:
        yield Header()
        with Horizontal():
            for _ in range(5):
                with Vertical():
                    for i in range(8):
                        if i % 2:
                            yield RadioSet(*[f"Choice {n+1}" for n in range(10)])
                        else:
                            yield Input(placeholder="Some other widget")
        yield Footer()


if __name__ == "__main__":
    RadioSetReduxApp().run()
