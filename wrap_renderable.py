"""Example of Static wrapping renderables."""

from textual.app import App, ComposeResult
from textual.containers import Grid
from textual.widgets import Static

TEXT = """[red]I must not fear.[/]
[green]Fear is the mind-killer.[/]
[blue]Fear is the little-death that brings total obliteration.[/]
[yellow]I will face my fear.[/]
[bold]I will permit it to pass over me and through me.[/]
[reverse]And when it has gone past, I will turn the inner eye to see its path.[/]
[yellow on red]Where the fear has gone there will be nothing. Only I will remain.[/]"""

class WrappingRenderableApp(App[None]):

    CSS = """
    Grid {
        grid-size: 3 1;
        grid-columns: 5fr 2fr 1fr;
    }

    Static {
        border: solid cornflowerblue;
    }
    """

    def compose(self) -> ComposeResult:
        with Grid():
            for _ in range(3):
                yield Static(TEXT)

if __name__ == "__main__":
    WrappingRenderableApp().run()

### wrap_renderable.py ends here
