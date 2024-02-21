from rich.align import Align

from textual.app import App, ComposeResult
from textual.widgets import TextLog


class TextLogApp(App[None]):

    CSS = """
    TextLog {
        border: panel cornflowerblue;
    }
    """

    def compose(self) -> ComposeResult:
        yield TextLog()

    def on_mount(self) -> None:
        log = self.query_one(TextLog)
        log.write("First line")
        log.write(" ")  # https://github.com/Textualize/textual/issues/3015
        log.write("Second line")
        log.write(Align.left("Left text"))
        log.write(Align.center("Center text"), expand=True, width=80)
        log.write(Align.right("Right text"), expand=True, width=80)


if __name__ == "__main__":
    TextLogApp().run()
