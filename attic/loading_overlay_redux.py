"""https://github.com/Textualize/textual/issues/3733"""

from textual.app import App, ComposeResult
from textual.widgets import OptionList


class LoadingOverlayRedux(App[None]):

    CSS = """
    OptionList {
        scrollbar-gutter: stable;
        width: 1fr;
        height: 1fr;
    }
    """

    BINDINGS = [("space", "toggle")]

    def compose(self) -> ComposeResult:
        yield OptionList(*[("X" * 500) for _ in range(1_000)])

    def action_toggle(self) -> None:
        self.query_one(OptionList).loading = not self.query_one(OptionList).loading


if __name__ == "__main__":
    LoadingOverlayRedux().run()

### loading_overlay_redux.py ends here
