"""Rainbow text."""

from itertools import cycle

from textual.app import App, ComposeResult
from textual.widgets import Label


class RainbowTextApp(App[None]):
    RAINBOW = cycle(
        (
            "E40303",
            "FF8C00",
            "FFED00",
            "008026",
            "24408E",
            "732982",
        )
    )

    def compose(self) -> ComposeResult:
        yield Label(
            "".join(
                f"[#{colour}]{letter}[/]"
                for colour, letter in zip(
                    self.RAINBOW, list("Fill the whole world with a rainbow")
                )
            )
        )


if __name__ == "__main__":
    RainbowTextApp().run()

### rainbow.py ends here
