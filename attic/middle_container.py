from textual.app import App, ComposeResult
from textual.containers import Horizontal, Middle
from textual.widgets import Input, Button


class MiddleContainerTestApp(App[None]):

    CSS = """
    Horizontal {
        height: auto;
    }

    Middle {
        height: 13;
    }

    Middle#input {
        width: 5fr;
    }

    Middle.buttons {
        width: 1fr;
    }

    #height-0 {
        height: 5;
    }

    #height-1 {
        height: 7;
    }

    #height-2 {
        height: 9;
    }

    #height-3 {
        height: 11;
    }

    #height-4 {
        height: 13;
    }
    """

    def compose(self) -> ComposeResult:
        for m in range(5):
            with Horizontal():
                with Middle(id="input"):
                    yield Input(str(m))
                for n in range(5):
                    with Middle(classes="buttons"):
                        yield Button(str(n), id=f"height-{n}")


if __name__ == "__main__":
    MiddleContainerTestApp().run()
