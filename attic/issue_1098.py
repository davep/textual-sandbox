"""Toying with issue 1098

https://github.com/Textualize/textual/issues/1098
"""

from json import dumps
from textual.app import App, ComposeResult
from textual.reactive import reactive
from textual.widgets import Input, Static


class Example(App):
    display_val = reactive({"input": ""}, always_update=True)

    def compose(self) -> ComposeResult:
        yield Input()
        yield Static()

    def on_input_changed(self, event: Input.Changed) -> None:
        self.display_val["input"] = event.value
        # WORKAROUND: Assign the reactive to itself to force a watch_.
        self.display_val = self.display_val

    def watch_display_val(self, new_display: dict) -> None:
        self.query_one(Static).update(dumps(new_display))


Example().run()
