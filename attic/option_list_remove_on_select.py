"""https://github.com/Textualize/textual/issues/3270"""

from textual import on
from textual.app import App, ComposeResult
from textual.widgets import OptionList

class OptionListRemoveOnDeleteApp(App[None]):

    def compose(self) -> ComposeResult:
        yield OptionList(*[f"This is option {n}" for n in range(20)])

    @on(OptionList.OptionSelected)
    def remove_option(self, event: OptionList.OptionSelected) -> None:
        options = self.query_one(OptionList)
        if event.option_index == (options.option_count - 1):
            options._mouse_hovering_over = None
        options.remove_option_at_index(event.option_index)

if __name__ == "__main__":
    OptionListRemoveOnDeleteApp().run()

### option_list_remove_on_select.py ends here
