"""Example of filtering an Input.

For a question on Discord.
"""

from textual.app import App, ComposeResult
from textual.events import Key
from textual.widgets import Input

class NoVowelsInput(Input):

    async def _on_key(self, event: Key) -> None:
        if event.character is not None and event.character.lower() in "aeiou":
            event.prevent_default()

class FilterInputApp(App[None]):

    def compose(self) -> ComposeResult:
        yield NoVowelsInput()

if __name__ == "__main__":
    FilterInputApp().run()

### filter_input.py ends here
