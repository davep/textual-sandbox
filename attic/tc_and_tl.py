from textual.app import App, ComposeResult
from textual.widgets import TabbedContent, TabPane, Label, TextLog


class TextLogInTabPane(App[None]):

    CSS = """
    TabbedContent ContentSwitcher {
        height: 1fr;
    }
    """

    def compose(self) -> ComposeResult:
        with TabbedContent():
            with TabPane("Logs"):
                yield Label("LABEL")
                yield TextLog()

    def on_mount(self) -> None:
        text_log = self.query_one(TextLog)
        for n in range(1000):
            text_log.write(f"{n} This is a log line {n}")


if __name__ == "__main__":
    TextLogInTabPane().run()
