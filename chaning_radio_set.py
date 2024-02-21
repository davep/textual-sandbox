"""https://github.com/Textualize/textual/discussions/3983"""

from textual import on
from textual.app import App, ComposeResult
from textual.containers import Vertical
from textual.widgets import RadioSet, Select


class DynamicRadioSetApp(App[None]):

    def compose(self) -> ComposeResult:
        yield Select[int]((("The Beatles", 0), ("Radiohead", 1), ("REM", 2)))
        with Vertical(id="band-picker"):
            yield RadioSet()

    @on(Select.Changed)
    async def pick_the_best_member(self, event: Select.Changed) -> None:
        set_container = self.query_one("#band-picker")
        await set_container.query_one(RadioSet).remove()
        members = []
        if event.value == 0:
            members = ["John", "Paul", "George", "Ringo"]
        elif event.value == 1:
            members = ["Thom", "Jonny", "Ed", "Philip"]
        elif event.value == 2:
            members = ["Bill", "Peter", "Mike", "Michael"]
        await set_container.mount(RadioSet(*members))


if __name__ == "__main__":
    DynamicRadioSetApp().run()

### chaning_radio_set.py ends here
