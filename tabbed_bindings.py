"""An example of specific bindings for specific tabs.

For a question on Discord.
"""

from textual.app import App, ComposeResult
from textual.binding import Binding
from textual.widgets import Footer, OptionList, TabbedContent, TabPane


class FooTab(TabPane):
    BINDINGS = [
        Binding("f1", "gndn", "Does a Foo"),
    ]

    def compose(self) -> ComposeResult:
        yield OptionList(*[f"Foo {n}" for n in range(100)])


class BarTab(TabPane):
    BINDINGS = [
        Binding("f1", "gndn", "Does a Bar"),
    ]

    def compose(self) -> ComposeResult:
        yield OptionList(*[f"Bar {n}" for n in range(100)])


class BazTab(TabPane):
    BINDINGS = [
        Binding("f1", "gndn", "Does a Baz"),
    ]

    def compose(self) -> ComposeResult:
        yield OptionList(*[f"Baz {n}" for n in range(100)])


class TabbedBindingsApp(App[None]):
    CSS = """
    OptionList {
        height: 1fr;
    }
    """

    def compose(self) -> ComposeResult:
        with TabbedContent():
            yield FooTab("Foo")
            yield BarTab("Bar")
            yield BazTab("Baz")
        yield Footer()


if __name__ == "__main__":
    TabbedBindingsApp().run()

### tabbed_bindings.py ends here
