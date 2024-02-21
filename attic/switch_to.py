"""Example for https://discord.com/channels/1026214085173461072/1033754296224841768/1075881301804073115"""

from textual.app import App, ComposeResult
from textual.containers import Vertical
from textual.widgets import Header, Footer, Label
from textual.widget import Widget


async def switch_to_widget(widget: Widget, parent: Widget):
    if widget.parent is None:
        await parent.mount(widget)
    else:
        widget.display = True


class SwitchTest(App[None]):

    CSS = """
    .hidden {
        display: none;
    }
    """

    BINDINGS = [
        ("1", "display", "Display the hidden widget"),
        ("2", "mount", "Maybe mount the unmounted widget"),
    ]

    def compose(self) -> ComposeResult:
        yield Header()
        yield Vertical(Label("This wasn't displayed", classes="hidden"))
        yield Footer()

    def on_mount(self) -> None:
        self.label = Label("This wasn't mounted")

    async def action_display(self) -> None:
        await switch_to_widget(self.query_one(".hidden"), self.query_one(Vertical))

    async def action_mount(self) -> None:
        await switch_to_widget(self.label, self.query_one(Vertical))


if __name__ == "__main__":
    SwitchTest().run()
