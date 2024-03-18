from itertools import cycle

from textual.app import App, ComposeResult
from textual.widgets import Label, TabbedContent, TabPane

LABELS = cycle(
    (
        "Johnny Silverhand",
        "Kerry Eurodyne",
        "Nancy Hartley",
        "Denny",
        "Henry",
        "V",
    )
)


class TCRenameApp(App[None]):
    BINDINGS = [
        ("space", "rename"),
    ]

    def compose(self) -> ComposeResult:
        with TabbedContent():
            with TabPane(next(LABELS), id="one"):
                yield Label("Press space to change my Tab's label")
            with TabPane("Two", id="two"):
                yield Label("This one won't rename")

    def action_rename(self) -> None:
        self.query_one(TabbedContent).get_tab("one").label = next(LABELS)


if __name__ == "__main__":
    TCRenameApp().run()

### content_tab_relabel.py ends here
