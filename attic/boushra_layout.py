from textual.app import App, ComposeResult
from textual.containers import Container, Vertical, Horizontal
from textual.widgets import Button, Input, Header, Footer

class LayoutExampleApp(App[None]):

    CSS = """
    Screen {
        align: center middle;
    }

    #background-panel {
        width: 80%;
        height: 80%;
        border: solid green;
        align: center middle;
    }

    #input-area {
        width: 80%;
        height: auto;
        border: solid orange;
    }

    #buttons {
        height: auto;
        align-horizontal: center;
    }

    Button {
        margin: 1;
    }
    """

    def compose(self) -> ComposeResult:
        yield Header()
        with Container(id="background-panel"):
            with Vertical(id="input-area"):
                yield Input(placeholder="Input something here")
                with Horizontal(id="buttons"):
                    yield Button("One")
                    yield Button("Two")
                    yield Button("Three")
                    yield Button("Four")
                    yield Button("Five")
        yield Footer()

if __name__ == "__main__":
    LayoutExampleApp().run()
