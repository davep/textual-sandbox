from textual import on
from textual.app import App, ComposeResult
from textual.widgets import Label, Select


class SelectTestApp(App[None]):

    def compose(self) -> ComposeResult:
        yield Select[bool]((("Aye", True), ("Naw", False)))
        yield Label("Make your mind up!")

    @on(Select.Changed)
    def decided(self, event: Select.Changed) -> None:
        if event.value is None:
            self.query_one(Label).update("Oh come on make a decision!")
        else:
            self.query_one(Label).update("Aye" if event.value else "Naw")


if __name__ == "__main__":
    SelectTestApp().run()

### select_none.py ends here
