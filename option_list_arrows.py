"""Adding arrows to the OptionList highlight."""

from rich.segment import Segment
from textual.app import App, ComposeResult
from textual.strip import Strip
from textual.widgets import OptionList


class ArrowList(OptionList):
    def render_line(self, y: int) -> Strip:
        _, scroll_y = self.scroll_offset
        line_number = scroll_y + y
        line = super().render_line(y)
        return Strip.join(
            [Strip([Segment("> ")]), line, Strip([Segment(" <")])]
            if self.highlighted is not None
            and line_number in self._spans[self.highlighted]
            else [Strip([Segment("  ")]), line, Strip([Segment("  ")])]
        ).simplify()

    def _left_gutter_width(self) -> int:
        # Twice the left to make up for the right too.
        return 4


class OptionListArrowApp(App[None]):
    def compose(self) -> ComposeResult:
        yield ArrowList(*[f"This is option {n}" for n in range(1_000)])


if __name__ == "__main__":
    OptionListArrowApp().run()

### option_list_arrows.py ends here
