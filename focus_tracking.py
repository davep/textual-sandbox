from textual.app import App, ComposeResult
from textual.widgets import TextArea


class TerminalFocusApp(App):
    def on_mount(self) -> None:
        # enable xterm focus tracking
        self._driver.write("\033[?1004h\n")  # type: ignore

    def compose(self) -> ComposeResult:
        # If the above xterm focus tracking is working, the TextArea should
        # show the unhandled FocusIn/FocusOut escape sequences after the
        # terminal window loses then gains focus
        yield TextArea()

    async def _on_exit_app(self) -> None:
        # disable xterm focus tracking again!
        self._driver.write("\033[?1004l\n")  # type: ignore


if __name__ == "__main__":
    app = TerminalFocusApp()
    app.run()
