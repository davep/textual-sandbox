"""Example of awaiting a mount and then scrolling."""

from textual.app import App, ComposeResult
from textual.containers import VerticalScroll
from textual.widgets import Input, Label


class AddAndScrollApp(App[None]):
    def compose(self) -> ComposeResult:
        with VerticalScroll() as scroller:
            scroller.can_focus = False
            yield Label("Press enter for more stuff")
            yield Input()

    async def on_input_submitted(self) -> None:
        await self.query_one(VerticalScroll).mount_all(
            [Label("Still press enter for more stuff"), new_input := Input()]
        )
        new_input.focus()
        self.query_one(VerticalScroll).scroll_end(animate=False)


if __name__ == "__main__":
    AddAndScrollApp().run()

### add_and_scroll.py ends here
