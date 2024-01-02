"""https://github.com/Textualize/textual/discussions/3943"""

from textual import on
from textual.app import App, ComposeResult
from textual.widgets import Input, Checkbox

class FocusNextOnSubmutApp(App[None]):

    def compose(self) -> ComposeResult:
        for n in range(10):
            if n == 5:
                yield Checkbox("We'll skip this!")
            else:
                yield Input(placeholder=f"This is input {n}")

    @on(Input.Submitted)
    def go_next(self) -> None:
        self.screen.focus_next(Input)

if __name__ == "__main__":
    FocusNextOnSubmutApp().run()

### focus_next_on_enter.py ends here
