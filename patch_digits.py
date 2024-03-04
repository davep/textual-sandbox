"""Example of patching digits.

For a question on Discord.
"""

from textual.app import App, ComposeResult
from textual.renderables import digits
from textual.widgets import Digits

digits.DIGITS = " 9876543210+-^x:"


class PatchDigitsApp(App[None]):
    def compose(self) -> ComposeResult:
        yield Digits("0123456789")


if __name__ == "__main__":
    PatchDigitsApp().run()

### patch_digits.py ends here
