from textual.app import App, ComposeResult
from textual.widgets import LoadingIndicator, Footer, Static


class LoadingApp(App[None]):

    CSS = """
    #one {
        height: 1;
    }

    #two {
        height: 2;
    }

    #three {
        height: 3;
    }

    Static {
        border: solid red;
    }

    LoadingIndicator {
        height: 1fr;
        border: solid green;
    }
    """

    def compose(self) -> ComposeResult:
        yield Static("One", id="one")
        yield Static("Two", id="two")
        yield Static("Three", id="three")
        yield LoadingIndicator()
        yield Footer()


if __name__ == "__main__":
    LoadingApp().run()

### li_in_middle.py ends here
