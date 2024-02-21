from textual.app import App, ComposeResult
from textual.widgets import TabbedContent, TabPane, Label, Footer


class TabbedContentRemoveBug(App[None]):

    BINDINGS = [
        ("delete", "delete"),
    ]

    def compose(self) -> ComposeResult:
        with TabbedContent():
            with TabPane("Keep me", id="keep-me"):
                yield Label("Keep me")
            with TabPane("Keep me", id="keep-me-too"):
                yield Label("Keep me too")
            with TabPane("Remove me", id="remove-me"):
                yield Label("Remove me")
        yield Footer()

    def action_delete(self) -> None:
        self.query_one(TabbedContent).remove_pane("remove-me")


if __name__ == "__main__":
    TabbedContentRemoveBug().run()
