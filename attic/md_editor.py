"""A minimal Markdown live preview scratchpad."""

from textual import on
from textual.app import App, ComposeResult
from textual.widgets import TextArea, Markdown


class MDEditor(App[None]):

    CSS = """
    Screen {
        layout: horizontal;
    }

    Screen > * {
        width: 1fr;
    }
    """

    def compose(self) -> ComposeResult:
        yield TextArea(language="markdown")
        yield Markdown()

    @on(TextArea.Changed)
    def update_preview(self, event: TextArea.Changed) -> None:
        self.query_one(Markdown).update(event.text_area.text)


if __name__ == "__main__":
    MDEditor().run()

### md_editor.py ends here
