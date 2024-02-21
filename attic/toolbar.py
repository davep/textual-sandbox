from textual.app import App, ComposeResult
from textual.widget import Widget
from textual.widgets import Button


class ToolbarButton(Button):

    DEFAULT_CSS = """
    ToolbarButton {
        width: auto;
        height: auto;
        border: none;
        min-width: 0;
    }

    ToobarButton:focus, ToolbarButton.-active {
        border: none;
    }
    """


class Toolbar(Widget):

    DEFAULT_CSS = """
    Toolbar {
        dock: bottom;
        layout: horizontal;
        height: auto;
    }
    """


class ExampleToolbarApp(App[None]):

    def compose(self) -> ComposeResult:
        with Toolbar():
            yield ToolbarButton("This")
            yield ToolbarButton("Is")
            yield ToolbarButton("An")
            yield ToolbarButton("Example")


if __name__ == "__main__":
    ExampleToolbarApp().run()

### toolbar.py ends here
