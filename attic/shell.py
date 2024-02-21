import os

from textual.app import App, ComposeResult
from textual.widgets import Header, Footer, Label


class ShellApp(App[None]):

    CSS = """
    Screen {
        align: center middle;
    }
    """

    BINDINGS = [("s", "shell", "Drop to a shell")]

    def compose(self) -> ComposeResult:
        yield Header()
        yield Label("Press S to drop to a shell")
        yield Footer()

    def action_shell(self) -> None:
        """Drop to a shell"""
        with self.suspend():
            os.system(os.environ.get("SHELL", "/bin/sh"))


if __name__ == "__main__":
    ShellApp().run()
