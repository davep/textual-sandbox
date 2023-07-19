from typing import cast

from textual.app import App, ComposeResult
from textual.containers import Vertical
from textual.widgets import Button, Label

class IntegerCargoButton(Button):

    def __init__(self, label: str, cargo: int) -> None:
        super().__init__(label)
        self.cargo = cargo

class CargoButtonApp(App[None]):

    def compose(self) -> ComposeResult:
        with Vertical():
            yield Label("Value will go here")
            for n in range(10):
                yield IntegerCargoButton(f"This is button {n}", n)

    def on_button_pressed(self, event: Button.Pressed) -> None:
        self.query_one(Label).update(f"You selected button {cast(IntegerCargoButton, event.button).cargo}")

if __name__ == "__main__":
    CargoButtonApp().run()
