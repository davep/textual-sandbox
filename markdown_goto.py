"""Test code for going to a heading in Markdown.

https://github.com/Textualize/textual/pull/4583
"""

from textual.app import App, ComposeResult
from textual.widgets import Markdown


class MarkdownGotoApp(App[None]):
    def compose(self) -> ComposeResult:
        yield Markdown(
            "\n\n".join(f"# Heading {n}\n\n" + ("XXXXX " * 1000) for n in range(100))
        )

    def on_mount(self) -> None:
        if self.query_one(Markdown).goto_anchor("heading-50"):
            self.notify("Markdown thinks we found and went to the anchor")
        else:
            self.notify("The anchor could not be found", severity="error")


if __name__ == "__main__":
    MarkdownGotoApp().run()

### markdown_goto.py ends here
