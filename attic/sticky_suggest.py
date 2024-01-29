"""https://github.com/Textualize/textual/issues/3806"""

from textual.app import App, ComposeResult
from textual.suggester import SuggestFromList
from textual.widgets import Input

class StickySuggestApp(App[None]):

    def compose(self) -> ComposeResult:
        for char in "ABCDEFGHIJ":
            yield Input(char, suggester=SuggestFromList([char * 30]))

if __name__ == "__main__":
    StickySuggestApp().run()

### sticky_suggest.py ends here
