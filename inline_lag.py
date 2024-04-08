"""Example of 0.56.2 inline mode widget lag."""

from textual.app import App, ComposeResult
from textual.widgets import Checkbox, Input


class InlineLagApp(App[None]):
    def compose(self) -> ComposeResult:
        yield Checkbox("Toggle this and note nothing happens")
        yield Input(
            placeholder="The above will update if you tab here, this will appear laggy to type into"
        )


if __name__ == "__main__":
    InlineLagApp().run(inline=True)

### inline_lag.py ends here
