"""https://github.com/Textualize/textual/discussions/3230"""

from textual.app import App, ComposeResult
from textual.widgets import TabbedContent, TabPane, Label, Input, Footer

class TestPane(TabPane):

    def compose(self) -> ComposeResult:
        for n in range(3):
            yield Label(f"Example input {n}")
            yield Input(placeholder=f"Example input {n}")

class DynamicTabbedContentApp(App[None]):

    BINDINGS = [
        ("a", "add", "Add a new test pane"),
        ("c", "clear", "Clear all the panes")
    ]

    def compose(self) -> ComposeResult:
        with TabbedContent():
            yield TestPane("First One")
        yield Footer()

    def action_add(self) -> None:
        self.query_one(TabbedContent).add_pane(TestPane("Another one"))

    def action_clear(self) -> None:
        self.query_one(TabbedContent).clear_panes()

if __name__ == "__main__":
    DynamicTabbedContentApp().run()

### dynamic_tabbed_content.py ends here
