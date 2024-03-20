"""Demonstrate that Markdown.update replaces the content."""

from textual.app import App, ComposeResult
from textual.widgets import Markdown


class MarkdownUpdate(App[None]):
    BINDINGS = [(str(n), f"md({n})") for n in range(10)]

    def compose(self) -> ComposeResult:
        yield Markdown()

    def action_md(self, number: int) -> None:
        self.query_one(Markdown).update(f"This is update {number}")


if __name__ == "__main__":
    MarkdownUpdate().run()

### markdown_update.py ends here
