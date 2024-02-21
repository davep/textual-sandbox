"""https://github.com/Textualize/textual/issues/1048"""

from textual.app import App, ComposeResult
from textual.widgets import Button, Static


class MyApp(App[None]):

    def compose(self) -> ComposeResult:
        yield Button("Push Me")
        yield Static("Push the above!", id="classes")

    def on_button_pressed(self, event: Button.Pressed) -> None:
        event.button.variant = (
            "warning" if event.button.variant == "default" else "default"
        )
        self.query_one("#classes", Static).update(", ".join(event.button.classes))


if __name__ == "__main__":
    MyApp().run()
