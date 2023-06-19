from textual.app import App, ComposeResult
from textual.containers import Horizontal, Vertical, VerticalScroll
from textual.events import Paste
from textual.widgets import Static, Markdown

from rich.markup import escape

class Document(Static):
    pass

class Tree(Static):
    pass

class MarkdownExplorerApp(App[None]):

    CSS = """
    VerticalScroll {
        border: panel $accent-darken-2;
    }

    VerticalScroll:focus {
        border: panel $accent;
    }

    Document, Markdown, Tree {
        height: auto;
        width: 1fr;
        margin: 0;
    }

    """

    def compose(self) -> ComposeResult:
        with Vertical():
            with VerticalScroll(id="document"):
                yield Document()
            with Horizontal():
                with VerticalScroll(id="markdown"):
                    yield Markdown()
                with VerticalScroll(id="tree"):
                    yield Tree()

    def on_mount(self) -> None:
        self.query_one("#document").border_title = "Markdown Document"
        self.query_one("#markdown").border_title = "Markdown Output"
        self.query_one("#tree").border_title = "Markdown Tree"
        self.query_one(Markdown).can_focus_children = False

    def on_paste(self, event: Paste) -> None:
        self.query_one(Document).update(escape(event.text))
        self.query_one(Markdown).update(event.text)
        self.call_after_refresh(
            self.query_one(Tree).update,
            self.query_one(Markdown).tree
        )

if __name__ == "__main__":
    MarkdownExplorerApp().run()
