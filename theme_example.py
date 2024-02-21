"""Example of theming an app via CSS."""

from textual import on
from textual.app import App, ComposeResult
from textual.widgets import Label, Select, Rule


class ExampleThemeApp(App[None]):

    CSS = """
    Label {
        border: solid white;
        width: 1fr;
        text-align: center;
    }

    App.theme-reds Label {
        border: solid red;
        background: red 20%;
        color: red;
    }

    App.theme-greens Label {
        border: solid green;
        background: green 20%;
        color: green;
    }

    App.theme-blues Label {
        border: solid blue;
        background: blue 20%;
        color: blue;
    }
    """

    THEMES = ("reds", "greens", "blues")

    def compose(self) -> ComposeResult:
        yield Select(((theme.capitalize(), theme) for theme in self.THEMES))
        yield Rule()
        for n in range(20):
            yield Label(f"This is example label {n}")

    @on(Select.Changed)
    def change_theme(self, event: Select.Changed) -> None:
        for theme in self.THEMES:
            self.set_class(event.value == theme, f"theme-{theme}")


if __name__ == "__main__":
    ExampleThemeApp().run()

### theme_example.py ends here
