from textual.app import App, ComposeResult
from textual.containers import Vertical
from textual.css.query import NoMatches
from textual.widgets import Button, Label


class ButtonApp(App[None]):

    BINDINGS = [
        ("f1", "button(1)"),
        ("f2", "button(2)"),
        ("f3", "button(3)"),
        ("f4", "button(4)"),
        ("f5", "button(5)"),
        ("f6", "button(6)"),
        ("f7", "button(7)"),
        ("f8", "button(8)"),
    ]

    def compose(self) -> ComposeResult:
        yield Label()
        with Vertical():
            for n in range(5):
                yield Button(f"This is button {n}", id=f"button-{n}")

    def action_button(self, button: int) -> None:
        try:
            self.query_one(f"#button-{button}", Button).press()
        except NoMatches:
            self.query_one(Label).update("That button doesn't exist")

    def on_button_pressed(self, event: Button.Pressed) -> None:
        self.query_one(Label).update(f"Pressed {event.button.id}")


if __name__ == "__main__":
    ButtonApp().run()
