"""Test changing directory tree path."""

from textual import on
from textual.app import App, ComposeResult
from textual.widgets import DirectoryTree, Input


class DirTreePathIssueApp(App[None]):
    def compose(self) -> ComposeResult:
        yield Input()
        yield DirectoryTree(".")

    @on(Input.Submitted)
    def new_path(self, event: Input.Submitted) -> None:
        self.notify(f"Swapping to {event.value}")
        self.query_one(DirectoryTree).path = event.value


if __name__ == "__main__":
    DirTreePathIssueApp().run()

### dir_tree_path_issue.py ends here
