from textual.app import App, ComposeResult
from textual.containers import Vertical
from textual.widgets import Header, Footer, RadioSet, RadioButton


class RSExternalChangeApp(App[None]):

    CSS = """
    Vertical {
        align: center middle;
    }

    RadioSet {
        padding: 2;
    }
    """

    BINDINGS = [("space", "next", "Next Radio Button")]

    def compose(self) -> ComposeResult:
        yield Header()
        with Vertical():
            yield RadioSet(
                *[
                    RadioButton(f"This is item {n}", not n, id=f"rb{n}")
                    for n in range(10)
                ]
            )
        yield Footer()

    def action_next(self):
        pressed = self.query_one(RadioSet).pressed_button
        next_rb = int(pressed.id.split("rb")[1])
        if next_rb == 9:
            next_rb = 0
        else:
            next_rb += 1
        self.query_one(f"#rb{next_rb}", RadioButton).toggle()


if __name__ == "__main__":
    RSExternalChangeApp().run()
