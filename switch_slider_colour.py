"""https://github.com/Textualize/textual/discussions/3354"""

from textual.app import App, ComposeResult
from textual.widgets import Switch

class SwitchSliderColourApp(App[None]):

    CSS = """
    Switch > .switch--slider {
        color: red;
    }

    Switch.-on > .switch--slider {
        color: yellow;
    }
    """

    def compose(self) -> ComposeResult:
        yield Switch()

if __name__ == "__main__":
    SwitchSliderColourApp().run()

### switch_slider_colour.py ends here
