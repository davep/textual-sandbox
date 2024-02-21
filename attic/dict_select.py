"""https://discord.com/channels/1026214085173461072/1033754296224841768/1168551342642565140"""

from textual.app import App, ComposeResult
from textual.widgets import SelectionList
from textual.widgets.selection_list import Selection


class SelectionListApp(App[None]):

    def make_selections(self, answer: list[dict[str, str]]) -> list[Selection]:
        selections: list[Selection] = []
        for item in answer:
            item_pair, *_ = list(item.items())
            selections.append(Selection(item_pair[1], item_pair[0]))
        return selections

    def compose(self) -> ComposeResult:
        answer = [{"item": "Hello"}, {"item2": "World"}, {"item3": "!"}]
        yield SelectionList[str](*self.make_selections(answer))


if __name__ == "__main__":
    SelectionListApp().run()

### dict_select.py ends here
