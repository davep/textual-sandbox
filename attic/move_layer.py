"""Example of moving widgets between layers."""

from textual.app import App, ComposeResult
from textual.widget import Widget


class MoveLayersApp(App[None]):
    CSS = """
    Screen {
        layers: bottom top;

        &.bottom-top {
            layers: top bottom;
        }
    }

    .box {
        width: 30;
        height: 15;
    }

    #red {
        background: red;
        offset-x: 15;
        offset-y: 7;
        layer: top;
    }

    #green {
        background: green;
        layer: bottom;
    }
    """

    BINDINGS = [
        ("space", "move"),
    ]

    def compose(self) -> ComposeResult:
        yield Widget(id="red", classes="box")
        yield Widget(id="green", classes="box")

    def action_move(self) -> None:
        self.screen.toggle_class("bottom-top")


if __name__ == "__main__":
    MoveLayersApp().run()

### move_layer.py ends here
