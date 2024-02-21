from textual.app import App, ComposeResult
from textual.containers import VerticalScroll
from textual.widgets import Header, Footer, Label


class ScrollingTextApp(App[None]):

    CSS = """
    Screen {
        align: center middle;
    }
    #chat {
        border: solid green;
        width: 50%;
        height: 50%;
    }
    """

    def compose(self) -> ComposeResult:
        yield Header()
        with VerticalScroll(id="chat"):
            yield Label("\n".join(f"This is line number {n}" for n in range(1_000)))
        yield Footer()


if __name__ == "__main__":
    ScrollingTextApp().run()
