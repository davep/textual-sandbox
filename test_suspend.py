from os import system
from code import InteractiveConsole
from time import time, sleep

from textual import on
from textual.app import App, ComposeResult, RenderResult, SuspendNotSupported
from textual.containers import Container
from textual.renderables.gradient import LinearGradient
from textual.widgets import Button

COLORS = [
    "#881177",
    "#aa3355",
    "#cc6666",
    "#ee9944",
    "#eedd00",
    "#99dd55",
    "#44dd88",
    "#22ccbb",
    "#00bbcc",
    "#0099cc",
    "#3366bb",
    "#663399",
]
STOPS = [(i / (len(COLORS) - 1), color) for i, color in enumerate(COLORS)]


class Splash(Container):

    DEFAULT_CSS = """
    Splash {
        layout: vertical;
        align: center middle;

        Button {
            width: 70%;
            margin-bottom: 2;
        }
    }
    """

    def on_mount(self) -> None:
        self.auto_refresh = 1 / 30

    def compose(self) -> ComposeResult:
        yield Button("Countdown", id="countdown")
        yield Button("Inputs", id="inputs")
        yield Button("REPL", id="repl")
        yield Button("Emacs", id="emacs")
        yield Button("vim", id="vim")

    def render(self) -> RenderResult:
        return LinearGradient(time() * 90, STOPS)

    @on(Button.Pressed, "#countdown")
    def countdown(self) -> None:
        try:
            with self.app.suspend():
                for n in reversed(range(10)):
                    print(n)
                    sleep(1)
        except SuspendNotSupported:
            self.notify("I'm sorry Dave, I'm afraid I can't do that", severity="error")

    @on(Button.Pressed, "#inputs")
    def inputs(self) -> None:
        try:
            with self.app.suspend():
                while True:
                    try:
                        data = input("Enter something (^D to quit): ")
                    except EOFError:
                        break
                    print(data)
        except SuspendNotSupported:
            self.notify("I'm sorry Dave, I'm afraid I can't do that", severity="error")

    @on(Button.Pressed, "#repl")
    def repl(self) -> None:
        try:
            with self.app.suspend():
                InteractiveConsole().interact()
        except SuspendNotSupported:
            self.notify("I'm sorry Dave, I'm afraid I can't do that", severity="error")

    @on(Button.Pressed, "#emacs")
    def emacs(self) -> None:
        try:
            with self.app.suspend():
                system("emacs -nw")
        except SuspendNotSupported:
            self.notify("I'm sorry Dave, I'm afraid I can't do that", severity="error")

    @on(Button.Pressed, "#vim")
    def vim(self) -> None:
        try:
            with self.app.suspend():
                system("vim")
        except SuspendNotSupported:
            self.notify("I'm sorry Dave, I'm afraid I can't do that", severity="error")


class SplashApp(App):

    def compose(self) -> ComposeResult:
        yield Splash()

    def on_resume(self) -> None:
        self.notify("WELCOME BACK!")

    def on_mount(self) -> None:
        self.app_resume_signal.subscribe(self, self.on_resume)


if __name__ == "__main__":
    SplashApp().run()
