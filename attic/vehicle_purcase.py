"""https://stackoverflow.com/questions/76722536/with-python-textual-package-how-do-i-linearly-switch-between-different-screen"""

from typing import Any

from textual import on
from textual.app import App, ComposeResult
from textual.widgets import Button, OptionList, Label, Checkbox, Pretty
from textual.widgets.option_list import Option
from textual.screen import ModalScreen


class SubScreen(ModalScreen):

    DEFAULT_CSS = """
    SubScreen {
        background: $panel;
        border: solid $boost;
    }
    """


class CarScreen(SubScreen):

    def compose(self) -> ComposeResult:
        yield Label("Buy a car!")
        yield Label("Lots of car-oriented widgets here I guess!")
        yield Button("Buy!", id="buy")
        yield Button("Cancel", id="cancel")

    @on(Button.Pressed, "#buy")
    def buy_it(self) -> None:
        self.dismiss({"options": "everything -- really we'd ask"})

    @on(Button.Pressed, "#cancel")
    def cancel_purchase(self) -> None:
        self.dismiss({})


class BikeScreen(SubScreen):

    def compose(self) -> ComposeResult:
        # Here we compose up the question screen for a bike.
        yield Label("Buy a bike!")
        yield Checkbox("Electric", id="electric")
        yield Checkbox("Mudguard", id="mudguard")
        yield Checkbox("Bell", id="bell")
        yield Checkbox("Wheels, I guess?", id="wheels")
        yield Button("Buy!", id="buy")
        yield Button("Cancel", id="cancel")

    @on(Button.Pressed, "#buy")
    def buy_it(self) -> None:
        # The user has pressed the buy button, so we make a structure that
        # has a key/value mapping of the answers for all the questions. Here
        # I'm just using the Checkbox; in a full application you'd want to
        # take more types of widgets into account.
        self.dismiss(
            {
                **{"type": "bike"},
                **{question.id: question.value for question in self.query(Checkbox)},
            }
        )

    @on(Button.Pressed, "#cancel")
    def cancel_purchase(self) -> None:
        # Cancel was pressed. So here we'll return no-data.
        self.dismiss({})


class VehiclePurchaseApp(App[None]):

    # Here you could create a structure of all of the types of vehicle, with
    # their names and the screen that asks the questions.
    VEHCILES: dict[str, tuple[str, type[ModalScreen]]] = {
        "car": ("Car", CarScreen),
        "bike": ("Bike", BikeScreen),
    }

    def compose(self) -> ComposeResult:
        # This builds the initial option list from the vehicles listed above.
        yield OptionList(
            *[
                Option(name, identifier)
                for identifier, (name, _) in self.VEHCILES.items()
            ]
        )
        # The `Pretty` is just somewhere to show the result. See
        # selection_made below.
        yield Pretty("")

    def selection_made(self, selection: dict[str, Any]) -> None:
        # This is the method that receives the selection after the user has
        # asked to buy the vehicle. For now I'm just dumping the selection
        # into a `Pretty` widget to show it.
        self.query_one(Pretty).update(selection)

    @on(OptionList.OptionSelected)
    def next_screen(self, event: OptionList.OptionSelected) -> None:
        # If the ID of the option that was selected is known to us...
        if event.option_id in self.VEHCILES:
            # ...create an instance of the screen associated with it, push
            # it and set up the callback.
            self.push_screen(
                self.VEHCILES[event.option_id][1](), callback=self.selection_made
            )


if __name__ == "__main__":
    VehiclePurchaseApp().run()
