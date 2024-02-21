from textual import on
from textual.app import App, ComposeResult
from textual.widgets import Button, Label


class RunAfterExitapp(App[None]):

    def compose(self) -> ComposeResult:
        yield Label("Press this button to exit")
        yield Button("Yes, that's right, this button")

    @on(Button.Pressed)
    def bye(self) -> None:
        self.exit()


if __name__ == "__main__":
    RunAfterExitapp().run()
    print("Hey! Welcome back!")

### run_after_exit.py ends here
