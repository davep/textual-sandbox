"""Example of a modal with a scrolling portion."""

from textual.app import App, ComposeResult
from textual.containers import Vertical, VerticalScroll
from textual.screen import ModalScreen
from textual.widgets import Button, Checkbox, Input, Label, TextArea


class Example(ModalScreen):
    CSS = """
    Example {
        align: center middle;
        Vertical {
            border: round cornflowerblue;
            width: 50%;
            height: 50%;
            TextArea {
                height: 10;
            }
        }
    }
    """

    def compose(self) -> ComposeResult:
        with Vertical():
            yield Label("This will not scroll")
            yield Button("Neither will this")
            with VerticalScroll() as scroller:
                scroller.can_focus = False
                for n in range(50):
                    yield Input(placeholder=f"Example input {n}")
                    yield Checkbox(f"This is Checkbox {n}")
                    yield TextArea(f"This is TextArea {n}", show_line_numbers=True)


class ScrollingStuffApp(App[None]):
    def on_mount(self) -> None:
        self.push_screen(Example())


if __name__ == "__main__":
    ScrollingStuffApp().run()

### scrolling_modal.py ends here
