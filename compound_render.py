from textual.app import App, ComposeResult, RenderResult
from textual.widget import Widget
from textual.widgets import Button

class ThisRendersAndComposes(Widget):

    DEFAULT_CSS = """
    ThisRendersAndComposes {
        align: center middle;
    }
    """

    def render(self) -> RenderResult:
        return f"[red]{'!' * self.size.width * self.size.height}[/]"

    def compose(self) -> ComposeResult:
        yield Button("DO NOT PRESS")

class CompoundRenderApp(App[None]):

    def compose(self) -> ComposeResult:
        yield ThisRendersAndComposes()

if __name__ == "__main__":
    CompoundRenderApp().run()
