from dataclasses import dataclass

from textual import on
from textual.app import App, ComposeResult
from textual.reactive import var
from textual.widgets import Button, RichLog


@dataclass
class ComplexThing:

    value: int = 0


class ForceWatchApp(App[None]):

    thing: var[ComplexThing] = var(ComplexThing, always_update=True)

    def compose(self) -> ComposeResult:
        yield Button("Push me to update the property")
        yield RichLog()

    def watch_thing(self) -> None:
        self.query_one(RichLog).write(f"Changed {self.thing!r}")

    @on(Button.Pressed)
    def update_thing(self) -> None:
        self.thing.value += 1
        self.thing = self.thing


if __name__ == "__main__":
    ForceWatchApp().run()
