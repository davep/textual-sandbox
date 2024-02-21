from textual.app import App, ComposeResult
from textual.widgets import Label


class H1(Label):
    pass


class NumberError(App[None]):

    CSS = """
    H1 {
        text-style: bold;
        color: yellow;
        background: red;
    }
    """

    def compose(self) -> ComposeResult:
        yield H1("This is a very important heading")


if __name__ == "__main__":
    NumberError().run()
