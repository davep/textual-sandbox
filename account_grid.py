"""Reactive grid example."""

from textual.app import App, ComposeResult
from textual.containers import Grid, ScrollableContainer
from textual.widgets import Button, Placeholder


class TUI(App):

    CSS = """
    .account {
        width: 1fr;
        height: 1fr;
    }

    Grid {
        grid-size: 5;
        grid-rows: 5;
        height: auto;
    }
    """

    def compose(self) -> ComposeResult:
        with ScrollableContainer(), Grid():
            for n in range(500):
                yield Placeholder(f"Account {n}", classes="account")
            yield Button("Add Account")

    def on_resize(self) -> None:
        # Calculate a fresh grid-size columns when we resize, adjust the
        # calculation to taste.
        self.query_one(Grid).styles.grid_size_columns = max(
            min(self.size.width // 30, 5), 1
        )


if __name__ == "__main__":
    TUI().run()

### account_grid.py ends here
