from textual.app import App, ComposeResult
from textual.widgets import Header, Footer, RadioSet, RadioButton, Label


class RadioSetButtonApp(App[None]):

    CSS = """
    Screen {
        align: center middle;
    }

    RadioSet {
        width: 50%;
    }
    """

    def compose(self) -> ComposeResult:
        yield Header()
        with RadioSet():
            yield RadioButton("One", name="One")
            yield RadioButton("Two", name="Two")
            yield RadioButton("Three", name="Three")
            yield RadioButton("Four", name="Four")
            yield RadioButton("Five", name="Five")
        yield Label("Press a radio button")
        yield Footer()

    def on_radio_set_changed(self, event: RadioSet.Changed):
        self.query_one(Label).update(
            f"Pressed: {event.pressed.label} named {event.pressed.name}"
        )


if __name__ == "__main__":
    RadioSetButtonApp().run()
