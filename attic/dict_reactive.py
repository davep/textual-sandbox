"""https://github.com/Textualize/textual/discussions/2538"""

from textual.app import App, ComposeResult
from textual.reactive import reactive
from textual.widgets import Header, Footer, Label


class DictReactiveApp(App[None]):

    my_dict = reactive(dict(), always_update=True, init=False)

    BINDINGS = [
        ("space", "change", ""),
    ]

    def compose(self) -> ComposeResult:
        yield Header()
        yield Label(str(self.my_dict))
        yield Footer()

    def watch_my_dict(self) -> None:
        self.query_one(Label).update(str(self.my_dict))

    def action_change(self) -> None:
        self.my_dict[len(self.my_dict)] = len(self.my_dict)
        self.my_dict = self.my_dict


if __name__ == "__main__":
    DictReactiveApp().run()
