from textual import on
from textual.app import App, ComposeResult
from textual.containers import VerticalScroll
from textual.widgets import Button, Label


class MaybeFocus(VerticalScroll, can_focus=False):

    def watch_show_vertical_scrollbar(self) -> None:
        self.can_focus = self.show_horizontal_scrollbar or self.show_vertical_scrollbar

    def watch_show_horizontal_scrollbar(self) -> None:
        self.can_focus = self.show_horizontal_scrollbar or self.show_vertical_scrollbar


class FocusWhenScrollApp(App[None]):

    CSS = """
    Label {
        height: 5;
        background: red;
        width: 1fr;
    }
    """

    def compose(self) -> ComposeResult:
        yield Button("MORE!")
        yield MaybeFocus()

    @on(Button.Pressed)
    def more(self) -> None:
        self.query_one(MaybeFocus).mount(Label("Stuff"))


if __name__ == "__main__":
    FocusWhenScrollApp().run()

### focus_when_scroll.py ends here
