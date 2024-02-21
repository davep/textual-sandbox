from textual.app import App, ComposeResult
from textual.containers import Horizontal, VerticalScroll
from textual.widgets import Button, Static


class ScrollAndFocusApp(App[None]):

    def compose(self) -> ComposeResult:
        with Horizontal():
            with VerticalScroll():
                for n in range(256):
                    yield Static(f"This is widget {n}")
            with VerticalScroll():
                yield Static("\n".join([f"This is line {n}" for n in range(256)]))
            with VerticalScroll() as buttons:
                buttons.can_focus = False
                for n in range(256):
                    yield Button(f"This is button {n}")


if __name__ == "__main__":
    ScrollAndFocusApp().run()
