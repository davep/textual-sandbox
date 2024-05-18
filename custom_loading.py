"""Example of a custom loading indicator."""

from textual.app import App, ComposeResult
from textual.containers import Vertical
from textual.widget import Widget
from textual.widgets import Label, LoadingIndicator, OptionList


class FancyLoading(Vertical):
    DEFAULT_CSS = """
    FancyLoading {
        LoadingIndicator, Label {
            height: 1fr;
            width: 1fr;
        }
        Label {
            content-align: center middle;
        }
    }
    """

    def compose(self) -> ComposeResult:
        yield LoadingIndicator()
        yield LoadingIndicator()
        yield LoadingIndicator()
        yield Label("So I'm just chilling here...")
        yield LoadingIndicator()
        yield LoadingIndicator()
        yield LoadingIndicator()


class CustomLoadingApp(App[None]):
    BINDINGS = [
        ("space", "loading"),
    ]

    def get_loading_widget(self) -> Widget:
        return FancyLoading()

    def compose(self) -> ComposeResult:
        yield OptionList(*[f"Here is fake option {n} " * 5 for n in range(1_000)])

    def action_loading(self) -> None:
        self.query_one(OptionList).loading = not self.query_one(OptionList).loading


if __name__ == "__main__":
    CustomLoadingApp().run()

### custom_loading.py ends here
