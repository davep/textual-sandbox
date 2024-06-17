"""Example for issue #4522"""

from textual.app import App, ComposeResult
from textual.containers import Grid
from textual.widgets import Label


def long_text() -> str:
    return 'aaa naa aaaaa aaa aaaan, aaa\naaa, aaaa?", aa aaa aaaaanaaa *anaaaaaaana* aaaaaaaa aaaaaana aaa aaaaa aa\naaa, aa *aaaaaaaaa* aaa aaaa, "aaaa, an *aaaa* aaa aaaa, a aa". "aaaa, naa\naaaaaaaaaaa, aaa a aaaa aaaaaanaa aaaa aa a aaa!", aaa anaaaa, aaaaa\naaaaaaaa aanaaaaa. "Na! aaa naa. aaaaa. aa aaaaa naa. aaaaa aa na aaa.",\naaa aaaaaaaa aaaanaaaaa DONE.\n'


class LongLabelApp(App[None]):
    CSS = """
    Grid {
        width: 60;
        border: solid red;
    }
    """

    def compose(self) -> ComposeResult:
        with Grid():
            yield Label(long_text(), shrink=True)


if __name__ == "__main__":
    LongLabelApp().run()

### long_label.py ends here
