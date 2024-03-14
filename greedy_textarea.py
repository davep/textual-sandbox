"""Example for https://github.com/Textualize/textual/issues/4292"""

from pathlib import Path

from textual.app import App, ComposeResult
from textual.widgets import Collapsible, TextArea


class GreedyScrollbarApp(App[None]):
    BINDINGS = [("f1", "collapse")]

    CSS = """
    TextArea {
        height: 10;
    }
    """

    def compose(self) -> ComposeResult:
        for n in range(5):
            with Collapsible(title=f"This is collapsible #{n}", collapsed=bool(n)):
                yield TextArea(Path(__file__).read_text(), language="python")

    def action_collapse(self) -> None:
        target.collapsed = not (target := self.query(Collapsible).first()).collapsed


if __name__ == "__main__":
    GreedyScrollbarApp().run()

### greedy_textarea.py ends here
