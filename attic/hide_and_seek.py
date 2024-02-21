from textual import on
from textual.app import App, ComposeResult
from textual.widgets import Label, Select


class HideAndSeek(App[None]):

    CSS = """
    .hidden {
        visibility: hidden;
    }
    """

    def compose(self) -> ComposeResult:
        yield Label("Here I am!", classes="hidden")
        yield Select[bool](
            (("Hidden", False), ("Visible", True)), value=False, allow_blank=False
        )

    @on(Select.Changed)
    def show_or_hide(self, event: Select.Changed) -> None:
        assert isinstance(event.value, bool)
        self.query_one(Label).set_class(not event.value, "hidden")


if __name__ == "__main__":
    HideAndSeek().run()

### hide_and_seek.py ends here
