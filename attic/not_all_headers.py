from textual.app import App, ComposeResult
from textual.screen import Screen
from textual.widgets import Header, Footer, Label


class First(Screen):

    BINDINGS = [("n", "switch_screen( 'second' )", "Second Screen")]

    def compose(self) -> ComposeResult:
        yield Header()
        yield Label("This is the first screen\n" "Notice the app title in the header.")
        yield Footer()


class Second(Screen):

    BINDINGS = [("n", "switch_screen( 'first' )", "First Screen")]

    def compose(self) -> ComposeResult:
        yield Header()
        yield Label(
            "This is the second screen\n"
            "Notice the total lack of app title in the header."
        )
        yield Footer()


class MultiScreen(App[None]):

    CSS = """
    Screen {
        align: center middle;
    }
    Label {
        width: auto;
    }
    """
    TITLE = "Very Cool App"

    SUB_TITLE = "These titles show off how proud I am about it"

    SCREENS = {"first": First, "second": Second}

    def on_compose(self) -> None:
        self.push_screen("first")


if __name__ == "__main__":
    MultiScreen().run()
