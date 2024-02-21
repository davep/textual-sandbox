from textual.app import App, ComposeResult
from textual.containers import Vertical
from textual.widgets import Header, Footer, RadioSet


class RadioSetsApp(App[None]):

    CSS = """
    #horizontal {
        layout: horizontal;
    }
    #horizontal RadioButton {
        margin-right: 1;
    }
    """

    def compose(self) -> ComposeResult:
        yield Header()
        yield Vertical(
            RadioSet("One", "Two", "Three", id="default"),
            RadioSet("One", "Two", "Three", id="horizontal"),
        )
        yield Footer()


if __name__ == "__main__":
    RadioSetsApp().run()
