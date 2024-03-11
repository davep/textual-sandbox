"""Extending kill-to-end-of-line to be more Emacs-like."""

from textual.app import App, ComposeResult
from textual.widgets import TextArea


class TextAreaEx(TextArea):
    def action_delete_to_end_of_line(self) -> None:
        if self.selection.end != self.get_cursor_line_end_location():
            super().action_delete_to_end_of_line()
        else:
            self.action_delete_line()


class CtrlKApp(App[None]):
    def compose(self) -> ComposeResult:
        yield TextAreaEx()


if __name__ == "__main__":
    CtrlKApp().run()

### ctrl_k.py ends here
