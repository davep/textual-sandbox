"""For https://github.com/Textualize/textual/pull/3647

The PR doesn't really mention any code to recreate the problem, and neither
does it mention the environment. While I've asked for the latter this is an
attempt to write some code that might possibly create the setup they
mention, at least, perhaps?
"""

from textual.app import App, ComposeResult
from textual.widgets import Input

class InputFocusAoo(App[None]):

    def compose(self) -> ComposeResult:
        for n in range(20):
            yield Input(placeholder=str(n))

if __name__ == "__main__":
    InputFocusAoo().run()

### lotsainput.py ends here
