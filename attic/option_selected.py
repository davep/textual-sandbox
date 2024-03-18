"""Example of handling an option selected event."""

from textual import on
from textual.app import App, ComposeResult
from textual.widgets import Footer, Header, Label, OptionList


class OptionListApp(App[None]):
    def compose(self) -> ComposeResult:
        yield Header()
        yield OptionList(
            "Aerilon",
            "Aquaria",
            "Canceron",
            "Caprica",
            "Gemenon",
            "Leonis",
            "Libran",
            "Picon",
            "Sagittaron",
            "Scorpia",
            "Tauron",
            "Virgon",
        )
        yield Label("Nothing selected yet")
        yield Footer()

    @on(OptionList.OptionSelected)
    def test_function(self, event: OptionList.OptionSelected) -> None:
        self.query_one(Label).update(f"You selected {event.option_index}")


if __name__ == "__main__":
    OptionListApp().run()

### option_selected.py ends here
