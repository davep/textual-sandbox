"""Subtle focus illustration."""

from textual.app import App, ComposeResult
from textual.widget import Widget


class MyWidget(Widget, can_focus=True):
    DEFAULT_CSS = """
    MyWidget {
        border-left: blank;
        background: #404040;
        padding-left: 1;
        width: 1fr;
        height: 1fr;
        color: $text;

        &:focus {
            border-left: thick $boost;
        }
    }
    """


class SubtleFocusApp(App[None]):
    def compose(self) -> ComposeResult:
        yield MyWidget()
        yield MyWidget()
        yield MyWidget()
        yield MyWidget()


if __name__ == "__main__":
    SubtleFocusApp().run()

### subtle_focus.py ends here
