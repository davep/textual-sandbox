"""Example of a nested CSS error."""

from textual.app import App, ComposeResult
from textual.widgets import Label


class NestedCSSTokenErrorApp(App[None]):
    CSS = """
    Label {
        &.foo, &.bar {
            border: solid red;
        }
    }
    """

    def compose(self) -> ComposeResult:
        yield Label("This is class foo", classes="foo")
        yield Label("This is class bar", classes="bar")


if __name__ == "__main__":
    NestedCSSTokenErrorApp().run()

### nested_css_token_error.py ends here
