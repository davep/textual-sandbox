"""Example of reacting to changes with a Select."""

from textual import on
from textual.app import App, ComposeResult
from textual.widgets import Label, Select

class SelectSomethingApp(App[None]):

    def compose(self) -> ComposeResult:
        yield Select[str](
            ((colour, colour.lower()) for colour in ("Red", "Green", "Blue"))
        )
        yield Label("Nothing selected yet")

    @on(Select.Changed)
    def colour_chosen(self, event: Select.Changed) -> None:
        if isinstance(event.value, str):
            self.screen.styles.background = event.value
            self.query_one(Label).update(event.value)

if __name__ == "__main__":
    SelectSomethingApp().run()

### select_react.py ends here
