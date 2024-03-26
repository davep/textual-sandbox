"""Tester for https://github.com/Textualize/textual/pull/4335"""

from textual.app import App, ComposeResult
from textual.suggester import SuggestFromList
from textual.widgets import Input


class SuggestTooSoon(App[None]):
    def compose(self) -> ComposeResult:
        for _ in range(10):
            yield Input(
                "TeX", suggester=SuggestFromList(["textual"], case_sensitive=False)
            )


if __name__ == "__main__":
    SuggestTooSoon().run()

### too_much_suggest.py ends here
