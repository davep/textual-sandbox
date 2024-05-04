"""Example of using a child screen to manipulate data."""

from textual import on, work
from textual.app import App, ComposeResult
from textual.containers import Horizontal
from textual.reactive import var
from textual.screen import Screen
from textual.widgets import Button


class SetDays(Screen[dict[str, bool]]):
    def __init__(self, selected_days: dict[str, bool]):
        super().__init__()
        self._selected_days = selected_days

    def compose(self) -> ComposeResult:
        with Horizontal():
            for day, selected in self._selected_days.items():
                yield Button(
                    day,
                    variant="success" if selected else "error",
                    classes="day",
                    id=day,
                )
            yield Button("Done", id="done")

    @on(Button.Pressed, ".day")
    def toggle_day(self, event: Button.Pressed) -> None:
        if event.button.id is not None:
            event.button.variant = (
                "error" if event.button.variant == "success" else "success"
            )
            self._selected_days[event.button.id] = event.button.variant == "success"

    @on(Button.Pressed, "#done")
    def return_days(self) -> None:
        self.dismiss(self._selected_days)


class DayButtonsApp(App[None]):
    selected_days: var[dict[str, bool]] = var(
        {
            "Monday": False,
            "Tuesday": False,
            "Wednesday": False,
            "Thursday": False,
            "Friday": False,
            "Saturday": False,
            "Sunday": False,
        }
    )

    def compose(self) -> ComposeResult:
        yield Button("Set Days", id="set-days")

    @on(Button.Pressed, "#set-days")
    @work
    async def set_days(self) -> None:
        self.selected_days = await self.push_screen_wait(SetDays(self.selected_days))


if __name__ == "__main__":
    DayButtonsApp().run()

### day_buttons.py ends here
