"""Using Rich markup in Textual."""

from textual.app import App, ComposeResult
from textual.widgets import Label


class RichMarkupApp(App[None]):

    def compose(self) -> ComposeResult:
        yield Label(
            "[red]But[/] [yellow on red]yes[/] you can use "
            "[black on green]Rich markup in Textual[/]"
        )


if __name__ == "__main__":
    RichMarkupApp().run()

### rich_colouring.py ends here
