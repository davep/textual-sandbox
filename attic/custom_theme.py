from textual.app import App, ComposeResult
from textual.widgets import Static

from rich.theme import Theme


class CustomThemeApp(App[None]):

    def on_mount(self) -> None:
        self.console.push_theme(Theme({"davep": "#000000 on #333333"}))

    def compose(self) -> ComposeResult:
        yield Static("This is [red]red[/] [dim red]and[/] this is [davep]davep[/]")


if __name__ == "__main__":
    CustomThemeApp().run()

### custom_theme.py ends here
