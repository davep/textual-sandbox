"""https://github.com/Textualize/textual/discussions/2376"""

from textual.app import App, ComposeResult
from textual.widgets import Footer, Header, OptionList, Label


class OptionListApp(App[None]):

    CSS = """
    Screen {
        align: center middle;
    }

    OptionList {
        background: $panel;
        border: round $primary;
        width: 70%;
        height: 70%;
    }
    """

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
        yield Label("Nothing has been selected yet")
        yield Footer()

    def on_mount(self) -> None:
        self.query_one(OptionList).focus()

    def on_option_list_option_selected(self, event: OptionList.OptionSelected) -> None:
        # Here we're showing the option that was selected.
        self.query_one(Label).update(f"You selected option {event.option_index}")

        # We could, of course, store the event.option_index into something
        # else here. There are other useful attributes too such as:
        #
        # - option: the option object itself
        # - option_id: The ID of the option, if it was given one.
        # - option_list: A reference to the option list that sent the message.


if __name__ == "__main__":
    OptionListApp().run()
