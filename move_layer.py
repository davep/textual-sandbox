"""Example of moving widgets between layers."""

from textual.app import App, ComposeResult
from textual.widget import Widget


class MoveLayersApp(App[None]):
    CSS = """
    Screen {
        layers: bottom top;
    }

    .box {
        width: 30;
        height: 15;
    }

    #red {
        background: red;
        offset-x: 15;
        offset-y: 7;
    }

    #green {
        background: green;
    }

    .top {
        layer: top;
    }

    .bottom {
        layer: bottom;
    }
    """

    BINDINGS = [
        ("space", "move"),
    ]

    def compose(self) -> ComposeResult:
        yield Widget(id="red", classes="box top")
        yield Widget(id="green", classes="box bottom")

    def action_move(self) -> None:
        self.query(".box").toggle_class("top").toggle_class("bottom")


if __name__ == "__main__":
    MoveLayersApp().run()

### move_layer.py ends here
