from textual.app import App, ComposeResult
from textual.containers import Grid
from textual.widgets import Static

class HardHeightGrid(App[None]):

    CSS = """
    Grid {
        grid-size: 5;
        grid-columns: 1fr 2fr 3fr 4fr 5fr;
        grid-rows: 1fr 2fr 3fr 4fr 5fr;
    }

    Static {
        border: round red;
        text-align: center;
        content-align: center middle;
        height: 1fr;
    }
    """

    def compose(self) -> ComposeResult:
        with Grid() as grid:
            grid.styles.height = 50
            for n in range(25):
                yield Static(f"This is grid cell {n}")

if __name__ == "__main__":
    HardHeightGrid().run()
