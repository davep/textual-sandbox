from textual.app import App, ComposeResult
from textual.containers import Vertical
from textual.widget import Widget
from textual.widgets import Header, Footer, Label


class ScrollApp(App[None]):

    BINDINGS = [("d", "decimate", "Decimate")]

    def widgets(self, count: int) -> list[Widget]:
        return [Label(f"This is label {n}", id=f"line{n}") for n in range(count)]

    def compose(self) -> ComposeResult:
        yield Header()
        yield Vertical(*self.widgets(500))
        yield Footer()

    async def action_decimate(self) -> None:
        widgets = self.query("Vertical > *")
        new_count = int(len(widgets) * 0.9)
        await widgets.remove()
        await self.query_one(Vertical).mount(*self.widgets(new_count))


if __name__ == "__main__":
    ScrollApp().run()
