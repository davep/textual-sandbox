"""Test scrolling through disabled widgets."""

from textual.app import App, ComposeResult
from textual.containers import VerticalScroll
from textual.widgets import Placeholder


class ScrollThroughDisabledApp(App[None]):
    CSS = """
    Placeholder {
        height: 10;
        margin: 1 2;
        &:disabled {
            opacity: 0.3;
        }
    }
    """

    def compose(self) -> ComposeResult:
        with VerticalScroll():
            for n in range(100):
                yield (placeholder := Placeholder())
                placeholder.disabled = bool(n % 2)


if __name__ == "__main__":
    ScrollThroughDisabledApp().run()

### scroll_through_disabled.py ends here
