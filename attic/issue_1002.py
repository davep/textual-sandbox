from textual.app import App, ComposeResult, RenderResult
from textual.widgets import Static
from textual.widget import Widget
from rich.table import Table
from rich.text import Text


class Info(Widget):
    def render(self):
        table = Table(show_header=False, expand=True, box=None, padding=0)
        table.add_column(justify="left", no_wrap=True)
        table.add_column(justify="right", no_wrap=True)
        table.add_row(Text.from_markup("[b]abc[/]"), Text.from_markup("[green]xyz[/]"))
        return table


class FooApp(App):
    CSS = """
    .box {
        width: 100%;
        border: white;
        height: 1;
    }
    """

    def compose(self) -> ComposeResult:
        yield Static("One [b]two[/] three", classes="box")
        yield Info(classes="box")


foo_app = FooApp()
foo_app.run()
