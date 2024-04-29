"""Example of a focus/scrolling problem.

https://github.com/Textualize/textual/issues/4461
"""

from textual.app import App, ComposeResult
from textual.containers import VerticalScroll
from textual.widgets import Input, Label


class Inner(Label, can_focus=True):
    DEFAULT_CSS = """
    Inner {
        width: 1fr;
        border: solid grey;
        &:focus {
            border: thick green;
        }
    }
    """


class Top(VerticalScroll, can_focus=False):
    def compose(self) -> ComposeResult:
        for n in range(100):
            yield Inner(f"{n}. This is a label that can get focus")


class ScrollFocusIssueApp(App[None]):
    AUTO_FOCUS = "Input"

    def compose(self) -> ComposeResult:
        yield Top()
        yield Input()

    def on_mount(self) -> None:
        self.query_one(Top).scroll_end(animate=False)


if __name__ == "__main__":
    ScrollFocusIssueApp().run()

### scroll_and_focus.py ends here
