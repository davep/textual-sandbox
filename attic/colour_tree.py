from textual.app import App, ComposeResult
from textual.widgets import Tree

from rich.highlighter import ReprHighlighter

class ColourTreeApp(App[None]):

    def compose(self) -> ComposeResult:
        yield Tree("Root")

    def on_mount(self) -> None:
        self.query_one(Tree).root.add_leaf(ReprHighlighter()("{'foo', 23, 'bar'}"))

if __name__ == "__main__":
    ColourTreeApp().run()

### colour_tree.py ends here
