"""Test code for https://github.com/Textualize/textual/issues/4274"""

from textual.app import App, ComposeResult
from textual.widgets import Collapsible, RichLog


class GreedyScrollbarApp(App[None]):
    BINDINGS = [("f1", "collapse")]

    CSS = """
    RichLog {
        height: 10;
    }
    """

    def compose(self) -> ComposeResult:
        for n in range(5):
            with Collapsible(title=f"This is collapsible #{n}", collapsed=bool(n)):
                yield (log := RichLog())
                for m in range(20):
                    log.write(f"Welcome to line number {m} in log {n}")

    def action_collapse(self) -> None:
        target.collapsed = not (target := self.query(Collapsible).first()).collapsed


if __name__ == "__main__":
    GreedyScrollbarApp().run()

### greedy_scrollbar.py ends here
