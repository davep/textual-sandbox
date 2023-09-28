from textual.app import App, ComposeResult
from textual.containers import Vertical
from textual.events import Click
from textual.screen import ModalScreen
from textual.widgets import Input, Button

class MyModal(ModalScreen[None]):

    DEFAULT_CSS = """
    MyModal {
        align: center middle;
    }

    MyModal > Vertical {
        width: 60%;
        height: 50%;
        border: panel cornflowerblue;
        background: $panel;
    }
    """

    def compose(self) -> ComposeResult:
        """Compose the child widgets."""
        with Vertical():
            yield Input()
            yield Input()
            yield Input()
            yield Button()

    def on_click(self, event: Click) -> None:
        self.notify(f"{self.get_widget_at(event.screen_x, event.screen_y)}")
        if self.get_widget_at(event.screen_x, event.screen_y)[0] is self:
            self.dismiss()

class OutsideModalApp(App[None]):

    def on_mount(self) -> None:
        self.push_screen(MyModal())

if __name__ == "__main__":
    OutsideModalApp().run()
