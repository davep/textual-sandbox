"""Example of handling non-local links with MarkdownViewer."""

from pathlib import Path
from webbrowser import open

from textual import on
from textual.app import App, ComposeResult
from textual.widgets import Markdown, MarkdownViewer


class LinkableMarkdownViewer(MarkdownViewer):

    @on(Markdown.LinkClicked)
    def handle_link(self, event: Markdown.LinkClicked) -> None:
        if not Path(event.href).exists():
            event.prevent_default()
            open(event.href)


class LinkyMDViewer(App[None]):

    def compose(self) -> ComposeResult:
        yield LinkableMarkdownViewer(
            """\
# Example document

[Here is a link](https://www.example.com/)
        """
        )


if __name__ == "__main__":
    LinkyMDViewer().run()

### linky_mv.py ends here
